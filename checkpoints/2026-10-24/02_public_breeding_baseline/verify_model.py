"""Exploratory model audit, 2026-10-24. Python 3 + numpy + scipy.

Exact rational identities are checked on the interior polynomial continuation.
Numerical optimization separately checks adoption corners and R&D deviations.
This is not an empirical calibration or a formal proof of general uniqueness.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import numpy as np
from scipy.optimize import minimize_scalar, differential_evolution


def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(B,q): return [dot(row,q) for row in B]


def exact_state(x, t, b, c, n, k, c0, delta, R, A=F(10),omega=F(1,2)):
    h=1-t; d=k+2*h; e=b+n-2*c; z=delta+h+b-c-c0
    a=[(d*(z+x[0])-e*(z+x[1]))/(d*d-e*e),
       (d*(z+x[1])-e*(z+x[0]))/(d*d-e*e)]
    B=[[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1]]
    q=[1-a[0],a[0],1-a[1],a[1]]
    alpha=[A,A+delta+x[0],A,A+delta+x[1]]
    p=[v-w for v,w in zip(alpha,mv(B,q))]
    ps=[dot(p[2*i:2*i+2],q[2*i:2*i+2])-c0*a[i]-k*a[i]*a[i]/2 for i in range(2)]
    cs=dot(q,mv(B,q))/2
    G=[ps[i]+omega*cs-R*x[i]*x[i]/2 for i in range(2)]
    W=sum(ps)+cs-R*dot(x,x)/2
    return a,G,W


def exact_derivative(f,x,i):
    # Exact for any quadratic polynomial; no floating point differences.
    xp=list(x);xm=list(x);xp[i]+=1;xm[i]-=1
    return (f(xp)-f(xm))/2


def rational_audit():
    count=0
    for t,b,c,n,k in [(F(1,2),F(3,5),F(3,10),F(3,5),F(1)),
                       (F(2,5),F(1,2),F(1,5),F(7,10),F(6,5)),
                       (F(3,5),F(7,10),F(1,2),F(2,5),F(4,5))]:
        for delta in [F(1,2),F(3,2)]:
            for x0 in [F(1,5),F(3,5)]:
                c0=F(1);R=F(2);x=[x0,x0]
                a,G,W=exact_state(x,t,b,c,n,k,c0,delta,R)
                h=1-t;d=k+2*h;e=b+n-2*c
                g=exact_derivative(lambda xx:exact_state(xx,t,b,c,n,k,c0,delta,R)[1][0],x,0)
                w=exact_derivative(lambda xx:exact_state(xx,t,b,c,n,k,c0,delta,R)[2],x,0)
                wedge=(h+c-b+(e-2*h)*a[0])/(2*(d-e))
                assert w==a[0]-R*x0
                assert g-w==wedge
                count+=1
    return count


def outside_consumer_audit():
    count=0
    for omega in [F(0),F(1,20),F(1,2)]:
        for delta in [F(4,5),F(17,10)]:
            t=F(1,2);b=n=F(3,5);c=F(9,20);k=F(1);c0=F(1);R=F(2);x=[F(1,5),F(1,5)]
            def state(xx):return exact_state(xx,t,b,c,n,k,c0,delta,R,omega=omega)
            a,_,_=state(x);h=1-t;d=k+2*h;e=b+n-2*c
            g=exact_derivative(lambda xx:state(xx)[1][0],x,0)
            w=exact_derivative(lambda xx:state(xx)[2],x,0)
            coefficient=(-2*h*d+e*e+omega*(2*h+e)*(d-e))/(d*d-e*e)
            assert coefficient<0
            assert g-w==coefficient*(a[0]-F(1,2))
            count+=1
    return count


def numerical_state(x,P,active=(True,True),fixed_cost=0.):
    t,b,c,n,k,c0,delta,R=P
    h=1-t;d=k+2*h;e=b+n-2*c;z=delta+h+b-c-c0
    M=np.array([[d,e],[e,d]])
    v=z+np.asarray(x)
    # Solve competitive allocation via its strictly convex potential, all 9 active sets.
    candidates=[]
    for status in product([-1,0,1],repeat=2):
        if any(not active[i] and status[i]!=-1 for i in range(2)): continue
        a=np.array([0. if s<=0 else 1. for s in status]);free=[i for i,s in enumerate(status) if s==0]
        fixed=[i for i,s in enumerate(status) if s!=0]
        if free:
            a[free]=np.linalg.solve(M[np.ix_(free,free)],v[free]-M[np.ix_(free,fixed)]@a[fixed])
        if np.all(a>=-1e-10) and np.all(a<=1+1e-10):
            grad=M@a-v
            if all((not active[i]) or (s==-1 and grad[i]>=-1e-9) or (s==1 and grad[i]<=1e-9) or (s==0 and abs(grad[i])<1e-9) for i,s in enumerate(status)):
                candidates.append(a)
    assert candidates
    a=candidates[0]
    B=np.array([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1]])
    q=np.array([1-a[0],a[0],1-a[1],a[1]])
    alpha=np.array([10,10+delta+x[0],10,10+delta+x[1]])
    p=alpha-B@q
    ps=np.array([p[2*i:2*i+2]@q[2*i:2*i+2]-c0*a[i]-k*a[i]**2/2 for i in range(2)])
    cs=q@B@q/2
    G=ps+cs/2-R*np.asarray(x)**2/2-fixed_cost*np.asarray(active)
    W=ps.sum()+cs-R*np.asarray(x)@np.asarray(x)/2-fixed_cost*sum(active)
    return a,G,W,p,np.linalg.eigvalsh(B)


def exhaustive_best_response(opponent_x,P,active=(True,True),fixed_cost=0.):
    """Enumerate every affine adoption regime; optimize each quadratic payoff piece."""
    t,b,c,n,k,c0,delta,R=P;h=1-t;d=k+2*h;e=b+n-2*c;z=delta+h+b-c-c0
    M=np.array([[d,e],[e,d]]);v0=np.array([z,z+opponent_x]);v1=np.array([1.,0.])
    upper=4.;breaks=[0.,upper]
    for status in product([-1,0,1],repeat=2):
        if any(not active[i] and status[i]!=-1 for i in range(2)):continue
        free=[i for i,s in enumerate(status) if s==0];fixed=[i for i,s in enumerate(status) if s!=0]
        a0=np.array([0. if s<=0 else 1. for s in status]);a1=np.zeros(2)
        if free:
            sub=M[np.ix_(free,free)]
            a0[free]=np.linalg.solve(sub,v0[free]-M[np.ix_(free,fixed)]@a0[fixed])
            a1[free]=np.linalg.solve(sub,v1[free])
        g0=M@a0-v0;g1=M@a1-v1
        linear=[]
        for i in free:linear.extend([(a0[i],a1[i]),(a0[i]-1,a1[i])])
        for i in fixed:linear.append((g0[i],g1[i]))
        for beta,alpha in linear:
            if abs(alpha)>1e-12 and 0<-beta/alpha<upper:breaks.append(float(-beta/alpha))
    breaks=sorted(set(breaks));candidates=list(breaks)
    def payoff(x):return numerical_state([x,opponent_x],P,active,fixed_cost)[1][0]
    for l,u in zip(breaks,breaks[1:]):
        m=(l+u)/2;step=(u-l)/4
        fm=payoff(m);fp=payoff(m+step);fn=payoff(m-step)
        second=(fp-2*fm+fn)/(step*step);first=(fp-fn)/(2*step)
        if second<0:
            opt=m-first/second
            if l<opt<u:candidates.append(opt)
    x=max(candidates,key=payoff)
    return float(x),float(payoff(x))


def run_examples():
    rows=[]
    # delta selects baseline advantage, holding every substitution and cost parameter fixed.
    for delta in [0.8,1.7]:
        P=(0.5,0.6,0.45,0.6,1.,1.,delta,2.)
        t,b,c,n,k,c0,delta,R=P;h=1-t;d=k+2*h;e=b+n-2*c;z=delta+h+b-c-c0
        H0=(h+c-b)/(2*(d-e));J=2*h-e;H1=1-J/(2*(d-e))
        xc=z/(R*(d+e)-1)
        xn=(H0*(d+e)+H1*z)/(R*(d+e)-H1)
        ac,_,wc,_,eig=numerical_state([xc,xc],P)
        an,gn,wn,p,_=numerical_state([xn,xn],P)
        # x>=d+e-z forces own adoption=1, after which marginal payoff=1-R*x.
        # Thus the [0,4] box covers every potentially optimal unilateral deviation.
        br_x,br_value=exhaustive_best_response(xn,P)
        opt=differential_evolution(lambda v:-numerical_state(v,P)[2],[(0,4),(0,4)],seed=19,tol=1e-11,polish=True)
        assert abs(br_x-xn)<1e-5
        assert max(abs(opt.x-np.array([xc,xc])))<1e-4
        assert all(p>0) and min(eig)>0
        B=np.array([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1]])
        inverse_B=np.linalg.inv(B)
        assert np.max(inverse_B[~np.eye(4,dtype=bool)])<0 # all goods gross substitutes
        rows.append(dict(delta=delta,x_local=xn,x_national=xc,adoption_local=float(an[0]),
                         adoption_national=float(ac[0]),W_local=float(wn),W_national=float(wc),
                         loss=float(wc-wn),best_response=br_x,
                         numerical_national_optimum=list(opt.x),min_demand_eigenvalue=float(min(eig)),
                         threshold=(h+c-b)/(2*h-e),parameters=list(P)))
    return rows


def release_audit():
    P=(0.5,0.6,0.45,0.6,1.,1.,0.8,2.)
    xn=run_examples()[0]['x_local']
    _,g_pair,w_pair,_,_=numerical_state([xn,xn],P)
    _,g_dev,_,_,_=numerical_state([0,xn],P,active=(False,True))
    retention=float(g_pair[0]-g_dev[0])
    _,_,w_none,_,_=numerical_state([0,0],P,active=(False,False))
    social={}
    for active in [(True,False),(True,True)]:
        ids=[i for i in range(2) if active[i]]
        def fun(z):
            x=np.zeros(2);x[ids]=z
            return -numerical_state(x,P,active=active)[2]
        res=differential_evolution(fun,[(0,4)]*len(ids),seed=4,tol=1e-12)
        social[str(active)]={'gross_W':float(-res.fun),'x':list(res.x),
                            'per_program_gain_over_none':float((-res.fun-w_none)/sum(active))}
    lower=max(v['per_program_gain_over_none'] for v in social.values())
    out=dict(retention_fixed_cost_upper=retention,no_program_national_W=float(w_none),
             social_profiles=social,no_program_optimal_if_F_above=lower)
    if lower<retention:
        Fcost=0.075
        assert lower<Fcost<retention
        out['counterexample_F']=Fcost
        out['net_nash_W']=float(w_pair-2*Fcost)
        out['absolute_welfare_loss']=float(w_none-w_pair+2*Fcost)
        out['strict_local_retention_margin']=retention-Fcost
        out['net_social_single_W']=social['(True, False)']['gross_W']-Fcost
        out['net_social_both_W']=social['(True, True)']['gross_W']-2*Fcost
        entry_x,entry_value=exhaustive_best_response(0.,P,active=(True,False),fixed_cost=Fcost)
        out['entry_x_against_no_program']=entry_x
        out['entry_gain_against_no_program']=entry_value-float(w_none/2)
        out['both_local_Nash']=[xn,xn]
    return out


if __name__=='__main__':
    out={'exact_rational_identity_checks':rational_audit(),
         'outside_consumer_exact_checks':outside_consumer_audit(),'examples':run_examples(),
         'release_game':release_audit(),
         'limitations':['The marginal wedge applies to the interior conditional on both programs operating; release_game separately checks the discrete participation margin.',
                       'Quality R&D only; no endogenous research direction or R&D success risk.',
                       'Numerical examples use equal regional consumer shares; outside_consumer_audit separately verifies the symmetric cross-generation case with nonproducing consumers. Identical tastes, fixed acreage and yield are maintained.',
                       'Global optimization checks are numerical, not uniqueness proofs.']}
    path=Path(__file__).with_name('verification_results.json')
    path.write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))
