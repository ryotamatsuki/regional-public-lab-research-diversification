"""Public breeding direction and cultivation rights. Exploratory audit, 2026-10-24.

Checks exact analytic payoff differences against independent competitive market
clearing, enumerates all research-direction deviations, and perturbs primitives.
Requires numpy and scipy. No empirical calibration or formal interval certificate.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize


def analytic_gains(p,rho,sigma,omega,delta):
    m=sigma-rho;b=1-rho
    return dict(exclusive_local=p*p*m*(1-omega)-p*delta,
                exclusive_national=p*p*m-p*delta,
                shared_local=p*p*m*(1-omega)-p*(1-p/2)*delta+p*p*omega*delta*delta/(4*b),
                shared_national=p*p*m-p*(2-p)*delta+p*p*delta*delta/(4*b))


def exact_state(choices,success,shared,values,rho,sigma,omega,old_value=F(4),old_sigma=F(17,20)):
    """Closed-form high-quality-regime state values; exact Fraction arithmetic."""
    if success==(0,0):
        ps=[old_value-1-old_sigma]*2;cs=1+old_sigma
        W=2*old_value-1-old_sigma
    elif sum(success)==1:
        i=success.index(1);v=values[choices[i]]
        if shared:
            ps=[v-2]*2;cs=F(2);W=2*v-2
        else:
            ps=[old_value-1-rho]*2;ps[i]=v-1-rho
            cs=1+rho;W=v+old_value-1-rho
    else:
        v1,v2=[values[c] for c in choices]
        same=choices[0]==choices[1];s=sigma if same else rho
        cs=1+s
        if shared:
            ps=[(v1+v2)/2-1-s]*2
            cs+=(v1-v2)**2/(4*(1-s))
        else:
            ps=[v1-1-s,v2-1-s]
        W=sum(ps)+cs
    G=[ps[i]+omega*cs for i in range(2)]
    return G,W


def exact_expected(choices,shared,p,values,rho,sigma,omega):
    G=[F(0),F(0)];W=F(0)
    for success in product((0,1),repeat=2):
        prob=p**sum(success)*(1-p)**(2-sum(success))
        g,w=exact_state(choices,success,shared,values,rho,sigma,omega)
        G=[G[i]+prob*g[i] for i in range(2)];W+=prob*w
    return G,W


def market_state(choices,success,shared,P):
    """Independent primal consumer-utility maximization / competitive equilibrium.

    Old varieties remain available and growers choose land allocations. They are
    not forced to plant the successful cultivar. Each grower region has fixed land.
    """
    vals=np.array(P['values'],float);rho=P['rho'];sigma=P['sigma'];omega=P['omega']
    old=np.array(P.get('old_values',[4.,4.]),float);land=np.array(P.get('land',[1.,1.]),float)
    old_sigma=P.get('old_sigma',.85);ys=np.array(P.get('new_yields',[1.,1.]),float)
    # descriptors: (owner, type, research direction, intercept)
    goods=[(0,'old',None,old[0]),(1,'old',None,old[1])]
    for i in range(2):
        if success[i]:goods.append((i,'new',choices[i],vals[choices[i]]))
    n=len(goods);B=np.full((n,n),rho);np.fill_diagonal(B,1.)
    B[0,1]=B[1,0]=old_sigma
    for j in range(2,n):
        for k in range(j+1,n):
            if goods[j][2]==goods[k][2]:B[j,k]=B[k,j]=sigma
    assert min(np.linalg.eigvalsh(B))>0
    alpha=np.array([g[3] for g in goods])
    flow=[]
    for i in range(2):
        flow.append((i,i))
        flow.extend((i,j) for j in range(2,n) if shared or goods[j][0]==i)
    M=np.zeros((n,len(flow)));L=np.zeros((2,len(flow)))
    for j,(i,k) in enumerate(flow):
        M[k,j]=1. if k<2 else ys[i]
        L[i,j]=1.
    x0=np.zeros(len(flow))
    for j,(i,k) in enumerate(flow):
        if k==i:x0[j]=land[i]
    def utility(x):
        q=M@x
        return alpha@q-.5*q@B@q
    def jac(x):return M.T@(alpha-B@(M@x))
    res=minimize(lambda x:-utility(x),x0,jac=lambda x:-jac(x),
                 constraints={'type':'eq','fun':lambda x:L@x-land,'jac':lambda x:L},
                 bounds=[(0,None)]*len(flow),method='SLSQP',options={'ftol':1e-12,'maxiter':200})
    assert res.success,res.message
    q=M@res.x;pvec=alpha-B@q
    ps=np.zeros(2)
    for j,(i,k) in enumerate(flow):ps[i]+=pvec[k]*M[k,j]*res.x[j]
    cs=.5*q@B@q
    # Check individual optimality: no farmer can improve per-acre revenue.
    revenue=M.T@pvec
    err=0.
    for i in range(2):
        ids=[j for j,(owner,k) in enumerate(flow) if owner==i]
        best=max(revenue[ids]);err=max(err,max((best-revenue[j]) for j in ids if res.x[j]>1e-6))
    assert err<2e-6,err
    G=ps+omega*cs
    return G,float(utility(res.x)),dict(q=q.tolist(),prices=pvec.tolist(),farm_surplus=ps.tolist(),CS=float(cs),KKT_error=float(err))


def expected(choices,shared,P):
    pvec=P.get('success_probabilities',[P['p'],P['p']]);G=np.zeros(2);W=0.
    for s in product((0,1),repeat=2):
        prob=np.prod([pvec[i] if s[i] else 1-pvec[i] for i in range(2)])
        g,w,_=market_state(choices,s,shared,P);G+=prob*g;W+=prob*w
    return G,W


def game(P,shared):
    K=len(P['values']);table={}
    for a in product(range(K),repeat=2):
        g,w=expected(a,shared,P);table[a]=(g,w)
    ne=[]
    for a,(g,w) in table.items():
        if all(g[i]>=table[tuple((b if j==i else a[j]) for j in range(2))][0][i]-1e-7
               for i in range(2) for b in range(K)):ne.append(list(a))
    best=max(v[1] for v in table.values())
    opt=[list(a) for a,v in table.items() if abs(v[1]-best)<1e-7]
    return dict(nash=ne,national_optima=opt,
                table={','.join(map(str,a)):{'G':g.tolist(),'W':w} for a,(g,w) in table.items()})


if __name__=='__main__':
    P=dict(p=.7,rho=.2,sigma=.9,omega=.2,values=[7.45,7.,6.7,6.4],old_values=[4.,4.],old_sigma=.85)
    pp=F(7,10);rr=F(1,5);ss=F(9,10);ww=F(1,5);dd=F(9,20)
    vv=[F(149,20),F(7)]
    gains=analytic_gains(pp,rr,ss,ww,dd)
    checks=0
    for shared in [False,True]:
        gAA,wAA=exact_expected((0,0),shared,pp,vv,rr,ss,ww)
        gBA,wBA=exact_expected((1,0),shared,pp,vv,rr,ss,ww)
        pref='shared' if shared else 'exclusive'
        assert gBA[0]-gAA[0]==gains[pref+'_local']
        assert wBA-wAA==gains[pref+'_national']
        for choices in product(range(2),repeat=2):
            for s in product((0,1),repeat=2):
                ge,we=exact_state(choices,s,shared,vv,rr,ss,ww)
                gn,wn,_=market_state(choices,s,shared,P)
                assert max(abs(gn-np.array(list(map(float,ge)))))<1e-6
                assert abs(wn-float(we))<1e-6
                checks+=1
    exclusive=game(P,False);shared=game(P,True)
    assert exclusive['nash']==[[0,0]]
    assert exclusive['national_optima']==[[0,1],[1,0]]
    assert shared['nash']==[[0,1],[1,0]]
    assert shared['national_optima']==[[0,0]]
    # Non-symmetric perturbations; keep 2 directions for efficient enumeration.
    perturb=[]
    for name,change in [('unequal_land',{'land':[1.02,.98]}),
                        ('unequal_success',{'success_probabilities':[.71,.69]}),
                        ('unequal_yield',{'new_yields':[1.01,.99]}),
                        ('different_old_values',{'old_values':[4.1,3.9]}),
                        ('demand_substitution',{'rho':.21,'sigma':.89})]:
        Q={**P,'values':P['values'][:2],**change};e=game(Q,False);s=game(Q,True)
        ok=e['nash']==[[0,0]] and e['national_optima'] in [[[0,1]],[[1,0]],[[0,1],[1,0]]] and s['nash']==[[0,1],[1,0]] and s['national_optima']==[[0,0]]
        assert ok,(name,e,s)
        perturb.append(dict(name=name,exclusive_nash=e['nash'],exclusive_optimum=e['national_optima'],shared_nash=s['nash'],shared_optimum=s['national_optima']))
    beta=1-P['rho'];m=P['sigma']-P['rho'];p=P['p'];omega=P['omega']
    critical=2/(1+np.sqrt(1+m/beta))
    T_shared=2*beta*((2-p)/p-np.sqrt(((2-p)/p)**2-m/beta))
    coef=[p*p*omega/(4*beta),-p*(1-p/2),p*p*m*(1-omega)]
    T_local=min(np.roots(coef))
    out=dict(parameters=P,exact_payoff_gain_checks={k:str(v) for k,v in gains.items()},
             independent_state_market_checks=checks,
             exclusive=exclusive,shared=shared,perturbations=perturb,
             thresholds=dict(exclusive_local=p*m*(1-omega),exclusive_national=p*m,shared_local=float(T_local),shared_national=float(T_shared),critical_success_probability=float(critical)),
             caveats=['Fixed committed research budgets, one project per laboratory, independent equal success probabilities in analytic benchmark.',
                      'High-quality regime: success induces full replacement on eligible land; adoption is chosen, not imposed.',
                      'Quadratic utility, fixed acreage; robust checks are finite numerical checks, not a global generality theorem.',
                      'No empirical calibration or proof that overall welfare falls after opening rights.',
                      'Potential research directions are finite and arbitrary; anonymous equal within/between-direction substitutability implies only the two best directions matter.'])
    path=Path(__file__).with_name('verified_results.json');path.write_text(json.dumps(out,indent=2))
    summary={k:v for k,v in out.items() if k not in ['exclusive','shared']}
    summary['equilibria']={regime:{k:out[regime][k] for k in ['nash','national_optima']} for regime in ['exclusive','shared']}
    print(json.dumps(summary,indent=2))
