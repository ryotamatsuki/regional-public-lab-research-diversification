"""Reproduce public breeding model checks, 2026-10-24.

Python 3, numpy and scipy. No empirical calibration is claimed.
Exact rational checks supplement the proofs in research_note_ja.md.
The zero-research counterexample uses exhaustive exact piecewise optimization.
Nonlinear demand checks are local interior derivative checks, not global Nash tests.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import numpy as np
from scipy.optimize import root


def dot(x, y):
    return sum(a*b for a,b in zip(x,y))


def matvec(A, x):
    return [dot(row,x) for row in A]


def solve(A,b):
    """Gaussian elimination over Fraction, including the empty system."""
    n=len(b)
    if not n:
        return []
    M=[list(A[i])+[b[i]] for i in range(n)]
    for k in range(n):
        j=next(j for j in range(k,n) if M[j][k])
        M[k],M[j]=M[j],M[k]
        z=M[k][k]
        M[k]=[v/z for v in M[k]]
        for j in range(n):
            if j!=k:
                z=M[j][k]
                M[j]=[v-z*w for v,w in zip(M[j],M[k])]
    return [row[-1] for row in M]


def block_B(N,t,b,c,n):
    return [[(1 if i==j else t) if i//2==j//2
             else (b if i%2==j%2==0 else n if i%2==j%2==1 else c)
             for j in range(2*N)] for i in range(2*N)]


def exact_general_identity():
    count=0
    for N,a,n,nonlinear in product([2,3,5],[F(1,4),F(1,2),F(3,4)],
                                  [F(1,2),F(3,5),F(7,10)],[False,True]):
        t,b,c=F(1,2),F(3,5),F(9,20)
        B=block_B(N,t,b,c,n)
        ksecond=F(1)+2*F(1,3)*a
        fprime=F(1) if not nonlinear else F(25,36) # f(x)=x/(1+x), x=1/5
        h=1-t;e=b+n-2*c
        H=[[ksecond+2*h if i==j else e for j in range(N)] for i in range(N)]
        da=solve(H,[fprime]+[F(0)]*(N-1))
        dq=[v for x in da for v in [-x,x]]
        q=[v for _ in range(N) for v in [1-a,a]]
        dp=[(fprime if j==1 else F(0))-v for j,v in enumerate(matvec(B,dq))]
        csprime=dot(q,matvec(B,dq))
        psprime=dot(q[:2],dp[:2])
        actual=psprime+csprime/N-fprime*a
        expected=fprime*F(N-1,N)*(h+c-b+(e-2*h)*a)/(ksecond+2*h-e)
        assert actual==expected
        assert np.linalg.eigvalsh(np.array(B,dtype=float)).min()>0
        count+=1
    return count


def exact_outside_consumers():
    count=0
    for N,a,share in product([2,3,5],[F(1,4),F(3,4)],[F(0),F(1,2),F(1)]):
        t,b,c,n=F(1,2),F(3,5),F(9,20),F(3,5)
        B=block_B(N,t,b,c,n);h=1-t;e=b+n-2*c;k=F(1)
        d=k+2*h;L=d-e;M=d+(N-1)*e;omega=share/N
        da=solve([[d if i==j else e for j in range(N)] for i in range(N)],
                 [F(1)]+[F(0)]*(N-1))
        dq=[v for x in da for v in [-x,x]]
        q=[v for _ in range(N) for v in [1-a,a]]
        dp=[(F(1) if j==1 else F(0))-v for j,v in enumerate(matvec(B,dq))]
        actual=dot(q[:2],dp[:2])+omega*dot(q,matvec(B,dq))-a
        J=2*h-e;S=2*h+(N-1)*e
        coef=F(N-1,N)*J/L+(F(1,N)-omega)*S/M
        assert actual==coef*(F(1,2)-a)
        assert coef>0
        count+=1
    return count


def linear_parameters(delta):
    return dict(N=2,t=F(1,2),b=F(3,5),c=F(9,20),n=F(3,5),
                k=F(1),k0=F(1),delta=delta,R=F(2),A=F(10))


def linear_state(x,P):
    N=P['N'];h=1-P['t'];e=P['b']+P['n']-2*P['c'];d=P['k']+2*h
    z=P['delta']+h+(N-1)*(P['b']-P['c'])-P['k0']
    H=[[d if i==j else e for j in range(N)] for i in range(N)]
    v=[z+u for u in x]
    found=[]
    for status in product([-1,0,1],repeat=N):
        a=[F(1) if s==1 else F(0) for s in status]
        free=[i for i,s in enumerate(status) if s==0]
        fixed=[i for i,s in enumerate(status) if s!=0]
        af=solve([[H[i][j] for j in free] for i in free],
                 [v[i]-sum(H[i][j]*a[j] for j in fixed) for i in free])
        for i,ai in zip(free,af): a[i]=ai
        grad=[u-w for u,w in zip(matvec(H,a),v)]
        if all(0<=ai<=1 for ai in a) and all(
                (g>=0 if s==-1 else g<=0 if s==1 else g==0)
                for s,g in zip(status,grad)):
            found=a;break
    assert found
    a=found;B=block_B(N,P['t'],P['b'],P['c'],P['n'])
    q=[v for ai in a for v in [1-ai,ai]]
    alpha=[v for xi in x for v in [P['A'],P['A']+P['delta']+xi]]
    p=[u-v for u,v in zip(alpha,matvec(B,q))]
    cs=dot(q,matvec(B,q))/2
    ps=[dot(q[2*i:2*i+2],p[2*i:2*i+2])-P['k0']*a[i]-P['k']*a[i]**2/2
        for i in range(N)]
    G=[ps[i]+cs/N-P['R']*x[i]**2/2 for i in range(N)]
    W=sum(ps)+cs-P['R']*dot(x,x)/2
    assert sum(G)==W
    return dict(a=a,G=G,W=W,p=p,cs=cs)


def exact_best_response(opponent,P,upper=F(4)):
    """All adoption regimes, boundaries and quadratic vertices on [0,upper]."""
    assert P['N']==2
    h=1-P['t'];e=P['b']+P['n']-2*P['c'];d=P['k']+2*h
    z=P['delta']+h+P['b']-P['c']-P['k0']
    H=[[d,e],[e,d]];v0=[z,z+opponent];v1=[F(1),F(0)]
    breaks={F(0),upper}
    for status in product([-1,0,1],repeat=2):
        fixed=[i for i,s in enumerate(status) if s!=0]
        free=[i for i,s in enumerate(status) if s==0]
        a0=[F(1) if s==1 else F(0) for s in status];a1=[F(0),F(0)]
        Hf=[[H[i][j] for j in free] for i in free]
        c0=solve(Hf,[v0[i]-sum(H[i][j]*a0[j] for j in fixed) for i in free])
        c1=solve(Hf,[v1[i] for i in free])
        for i,u,v in zip(free,c0,c1):a0[i]=u;a1[i]=v
        g0=[v-w for v,w in zip(matvec(H,a0),v0)]
        g1=[v-w for v,w in zip(matvec(H,a1),v1)]
        pairs=[]
        for i in free:pairs.extend([(a0[i],a1[i]),(a0[i]-1,a1[i])])
        for i in fixed:pairs.append((g0[i],g1[i]))
        for u,v in pairs:
            if v and 0<-u/v<upper:breaks.add(-u/v)
    breaks=sorted(breaks);candidates=set(breaks)
    def payoff(x): return linear_state([x,opponent],P)['G'][0]
    for lo,hi in zip(breaks,breaks[1:]):
        mid=(lo+hi)/2;step=(hi-lo)/4
        fm,fp,fn=payoff(mid),payoff(mid+step),payoff(mid-step)
        second=(fp-2*fm+fn)/step**2;first=(fp-fn)/(2*step)
        if second<0:
            vertex=mid-first/second
            if lo<vertex<hi:candidates.add(vertex)
    # For x beyond upper, own adoption is one, and payoff derivative is 1-R*x<0.
    assert upper>=d+max(e,0)-z and P['R']*upper>1
    best=max(candidates,key=payoff)
    return best,payoff(best),len(candidates)


def linear_equilibria():
    rows=[]
    for delta in [F(4,5),F(17,10),F(17,50)]:
        P=linear_parameters(delta);h=1-P['t'];e=P['b']+P['n']-2*P['c']
        d=P['k']+2*h;L=d-e;M=d+e;z=delta+h+P['b']-P['c']-P['k0']
        J=2*h-e;xi=J/(2*L);astar=(h+P['c']-P['b'])/J
        xn=((1-xi)*z+xi*astar*M)/(P['R']*M-1+xi)
        xc=max(F(0),z/(P['R']*M-1))
        local=linear_state([xn,xn],P);national=linear_state([xc,xc],P)
        br,value,count=exact_best_response(xn,P)
        assert br==xn and value==local['G'][0]
        no=linear_state([F(0),F(0)],P)
        dev=linear_state([F(0),xn],P)
        B=np.array(block_B(2,P['t'],P['b'],P['c'],P['n']),dtype=float)
        inverse=np.linalg.inv(B)
        assert np.max(inverse[~np.eye(4,dtype=bool)])<0
        # W is strongly concave in x for the constrained competitive allocation.
        assert P['R']>1/L
        if z<0:
            # Completing the square proves global zero research for every x>=0.
            assert min(L,M)>1/P['R']
            assert national['a']==[F(0),F(0)]
            assert local['W']<no['W']
            assert local['G'][0]>dev['G'][0]
            entry_x,entry_value,_=exact_best_response(F(0),P)
            assert entry_x>0 and entry_value>no['G'][0]
        rows.append(dict(delta=float(delta),z=float(z),x_local=float(xn),
                         x_local_exact=str(xn),x_national=float(xc),
                         adoption_local=float(local['a'][0]),
                         adoption_national=float(national['a'][0]),
                         W_local=float(local['W']),W_national=float(national['W']),
                         W_zero_effort_candidates_available=float(no['W']),
                         unilateral_exit_loss=float(local['G'][0]-dev['G'][0]),
                         unilateral_exit_loss_exact=str(local['G'][0]-dev['G'][0]),
                         global_best_response_exact=str(br),candidate_count=count,
                         min_eigenvalue=float(np.linalg.eigvalsh(B).min()),
                         largest_off_diagonal_inverse=float(inverse[~np.eye(4,dtype=bool)].max())))
        if z<0:
            rows[-1]['entry_effort_against_zero_exact']=str(entry_x)
            rows[-1]['entry_gain_against_zero_exact']=str(entry_value-no['G'][0])
    return rows


def phi(q,gamma,delta):
    if gamma==0:return delta*(q*np.log(q)-q)
    if gamma==-1:return -delta*np.log(q)
    return delta*q**(gamma+1)/(gamma*(gamma+1))


def phiprime(q,gamma,delta):
    if gamma==0:return delta*np.log(q)
    return delta*q**gamma/gamma


def nonlinear_state(x,P,initial):
    N=P['N'];gamma=P['gamma'];delta=P['delta']
    f=np.asarray(x)/(1+np.asarray(x))
    def equation(a):
        return (P['Delta']+f-phiprime(a,gamma,delta)+phiprime(1-a,gamma,delta)
                -P['g']*(2*np.sum(a)-N)-P['k0']-P['k']*a-P['nu']*a*a)
    def jacobian(a):
        diag=delta*(a**(gamma-1)+(1-a)**(gamma-1))+P['k']+2*P['nu']*a
        return -np.diag(diag)-2*P['g']*np.ones((N,N))
    sol=root(equation,initial,jac=jacobian,tol=1e-11)
    a=sol.x
    assert np.max(abs(equation(a)))<1e-9 and np.min(a)>0 and np.max(a)<1
    q=np.array([v for ai in a for v in [1-ai,ai]])
    total=q.sum();region=q.reshape(N,2).sum(axis=1);generation=q.reshape(N,2).sum(axis=0)
    alpha=np.array([v for fi in f for v in [P['A'],P['A']+P['Delta']+fi]])
    prices=(alpha-phiprime(q,gamma,delta)-P['beta']*total
            -P['r']*np.repeat(region,2)-P['g']*np.tile(generation,N))
    utility=(alpha@q-phi(q,gamma,delta).sum()-P['beta']*total**2/2
             -P['r']*(region@region)/2-P['g']*(generation@generation)/2)
    cs=utility-prices@q
    K=P['k0']*a+P['k']*a*a/2+P['nu']*a**3/3
    costs=P['R']*np.asarray(x)**2/2
    ps=np.sum(prices.reshape(N,2)*q.reshape(N,2),axis=1)-K
    G=ps+cs/N-costs;W=utility-K.sum()-costs.sum()
    assert abs(G.sum()-W)<1e-8
    return a,G,W,prices


def nonlinear_demand_checks():
    rows=[]
    for N,gamma,a in product([2,3,5],[-1.,0.,.5,1.,2.],[.25,.75]):
        P=dict(N=N,gamma=gamma,delta=.35,beta=1.5,r=.01,g=.01,
               k0=2.,k=1.,nu=.3,R=2.,A=30.)
        x=.2;fp=1/(1+x)**2
        P['Delta']=(P['k0']+P['k']*a+P['nu']*a*a-x/(1+x)
                    +phiprime(a,gamma,P['delta'])-phiprime(1-a,gamma,P['delta'])
                    +P['g']*N*(2*a-1))
        q=np.tile([1-a,a],N)
        B=np.diag(P['delta']*q**(gamma-1))+P['beta']*np.ones((2*N,2*N))
        B+=P['r']*np.kron(np.eye(N),np.ones((2,2)))
        B+=P['g']*np.kron(np.ones((N,N)),np.eye(2))
        S=np.kron(np.eye(N),np.array([[-1.],[1.]]))
        H=S.T@B@S+(P['k']+2*P['nu']*a)*np.eye(N)
        da=np.linalg.solve(H,np.eye(N)[0]*fp)
        dp=fp*np.eye(2*N)[1]-B@S@da
        actual=q[:2]@dp[:2]+(fp*a-q@dp)/N-fp*a
        L=P['k']+2*P['nu']*a+P['delta']*(a**(gamma-1)+(1-a)**(gamma-1))
        predicted=fp*(N-1)/N*P['delta']*((1-a)**gamma-a**gamma)/L
        assert abs(actual-predicted)<1e-12
        eps=1e-5;xp=np.full(N,x);xm=xp.copy();xp[0]+=eps;xm[0]-=eps
        sp=nonlinear_state(xp,P,np.full(N,a));sm=nonlinear_state(xm,P,np.full(N,a))
        finite=(sp[1][0]-sm[1][0]-sp[2]+sm[2])/(2*eps)
        assert abs(finite-predicted)<2e-6
        inverse=np.linalg.inv(B);maxoff=inverse[~np.eye(2*N,dtype=bool)].max()
        assert maxoff<0 and min(sp[3])>0 and min(sm[3])>0
        rows.append(dict(N=N,gamma=gamma,adoption=a,wedge=actual,
                         predicted=predicted,finite_difference=finite,
                         max_direct_demand_cross_price_slope=float(maxoff)))
    return rows


def budget_balanced_matching_grant():
    """Equal residents finance the national grant pool; real resource cost stays R."""
    rows=[]
    for delta in [F(4,5),F(17,10)]:
        P=linear_parameters(delta);N=P['N'];h=1-P['t'];e=P['b']+P['n']-2*P['c']
        d=P['k']+2*h;M=d+e;L=d-e;xi=(2*h-e)/(2*L)
        z=delta+h+P['b']-P['c']-P['k0']
        for rate in [F(0),F(1,10)]:
            effective=P['R']*(1-rate*F(N-1,N))
            x=((1-xi)*z+xi*F(1,2)*M)/(effective*M-1+xi)
            # In a unilateral deviation the grant-pool tax from the rival is constant.
            private=P.copy();private['R']=effective
            best,_,_=exact_best_response(x,private)
            assert best==x
            s=linear_state([x,x],P) # full real R&D cost, no transfer counted as benefit
            rows.append(dict(delta=float(delta),matching_rate=float(rate),
                             effort=float(x),national_welfare=float(s['W'])))
    assert rows[1]['national_welfare']<rows[0]['national_welfare']
    assert rows[3]['national_welfare']>rows[2]['national_welfare']
    return rows


if __name__=='__main__':
    out=dict(exact_general_identity_checks=exact_general_identity(),
             exact_outside_consumer_checks=exact_outside_consumers(),
             linear_equilibria=linear_equilibria(),
             nonlinear_demand_checks=nonlinear_demand_checks(),
             matching_grant_examples=budget_balanced_matching_grant(),
             scope=[
                 'Arbitrary N and convex adoption cost: analytical symmetric interior identities.',
                 'Global Nash checks: exact two-region quadratic examples only.',
                 'Nonlinear demand checks: local interior derivatives with competitive adoption.',
                 'Quality effort is endogenous; research direction and licensing policy are fixed.',
                 'Positive-baseline examples condition on available candidate varieties; zero effort need not mean no program.',
                 'Not a calibration, estimation, formal proof assistant verification, or publication guarantee.'])
    p=Path(__file__).with_name('verification_results.json')
    p.write_text(json.dumps(out,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in out.items() if k!='nonlinear_demand_checks'},indent=2))
    print('Nonlinear derivative checks:',len(out['nonlinear_demand_checks']))
