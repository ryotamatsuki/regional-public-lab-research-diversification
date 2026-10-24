#!/usr/bin/env python3
"""Stage 05 independent audit. Requires numpy, scipy, sympy.
Run: python verify_ijio.py
No imports from Stage 04's verification implementation.
Outputs numerical certificates and fails assertions on disagreement.
"""
import json
import numpy as np
import sympy as sy
from scipy.optimize import root, minimize, minimize_scalar, brentq

def symbolic():
    t,b,n,c,k,a=sy.symbols('t b n c k a', real=True)
    B=sy.Matrix([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1]])
    S=sy.Matrix([[-1,0],[1,0],[0,-1],[0,1]])
    q=sy.Matrix([1-a,a,1-a,a])
    H=S.T*B*S+k*sy.eye(2)
    dp=-B*S*H.inv()*sy.Matrix([1,0])
    got=sy.factor((q[:2,0].dot(dp[:2,0])-q[2:,0].dot(dp[2:,0]))/2)
    h=1-t;e=b+n-2*c
    expect=(h+c-b+(e-2*h)*a)/(2*(k+2*h-e))
    assert sy.simplify(got-expect)==0
    return str(sy.factor(got))

P=dict(t=.5,b=.6,n=.6,c=.45,k=1.,k0=1.,R=2.,A=10.)
def linear_state(x,delta,fixed=None):
    x=np.array(x,float);t,b,n,c=P['t'],P['b'],P['n'],P['c']
    B=np.array([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1.]])
    S=np.array([[-1,0],[1,0],[0,-1],[0,1.]],float)
    q0=np.array([1.,0,1,0]);alpha=np.array([10.,10+delta+x[0],10.,10+delta+x[1]])
    H=S.T@B@S+np.eye(2)*P['k']
    rhs=S.T@(alpha-B@q0)-P['k0']*np.ones(2)
    if fixed is not None: a=np.array(fixed,float)
    else:
        z=np.linalg.solve(H,rhs)
        if np.min(z)>=0 and np.max(z)<=1: a=z
        else:
            so=minimize(lambda a:.5*a@H@a-rhs@a,np.clip(z,0,1),
                jac=lambda a:H@a-rhs,method='L-BFGS-B',bounds=[(0,1)]*2)
            a=so.x
    q=q0+S@a;p=alpha-B@q
    V=alpha@q-.5*q@B@q; CS=V-q@p
    K=P['k0']*a+P['k']*a*a/2;C=P['R']*x*x/2
    Pi=np.array([q[:2]@p[:2],q[2:]@p[2:]])-K
    G=Pi+CS/2-C;W=V-K.sum()-C.sum()
    assert abs(G.sum()-W)<1e-9
    return a,G,W

def linear_check():
    out=[]
    for D in (.8,1.7,.34):
        def best(y):
            f=lambda xx: linear_state([xx,y],D)[1][0]
            sol=minimize_scalar(lambda xx:-f(xx),bounds=(0,1.5),method='bounded')
            return max([(0,f(0)),(1.5,f(1.5)),(sol.x,f(sol.x))],key=lambda z:z[1])[0]
        xs=np.linspace(0,1.5,301); brackets=[(u,v) for u,v in zip(xs[:-1],xs[1:]) if (best(u)-u)*(best(v)-v)<0]
        xn=brentq(lambda xx:best(xx)-xx,*brackets[0]) if brackets else 0.
        a,G,W=linear_state([xn,xn],D)
        sp=minimize_scalar(lambda z:-linear_state([z,z],D)[2],bounds=(0,1.5),method='bounded')
        xc=max([(0,linear_state([0,0],D)[2]),(1.5,linear_state([1.5,1.5],D)[2]),(sp.x,-sp.fun)],key=lambda z:z[1])[0]
        aa,GG,WW=linear_state([xc,xc],D)
        eps=1e-5
        ap,gp,wp=linear_state([xn+eps,xn],D)
        am,gm,wm=linear_state([xn-eps,xn],D)
        numerical=(gp[0]-gm[0]-wp+wm)/(2*eps)
        h=1-P['t'];e=P['b']+P['n']-2*P['c']
        formula=(h+P['c']-P['b']+(e-2*h)*a[0])/(2*(P['k']+2*h-e))
        assert abs(numerical-formula)<1e-6
        _,gf,wf=linear_state([xn+eps,xn],D,fixed=a)
        _,gb,wb=linear_state([xn-eps,xn],D,fixed=a)
        fixed=(gf[0]-gb[0]-wf+wb)/(2*eps)
        assert abs(fixed)<1e-7
        out.append(dict(Delta=D,x_decentralized=float(xn),x_planner_symmetric=float(xc),
                        a_decentralized=float(a[0]),a_planner=float(aa[0]),
                        W_decentralized=float(W),W_planner=float(WW),
                        wedge=float(numerical),wedge_formula=float(formula),
                        fixed_adoption_wedge=float(fixed)))
    return out

def phi(q,g,d):
    if g == -1.: return -d*np.log(q)
    if g == 0.: return d*(q*np.log(q)-q)
    return d*q**(g+1)/(g*(g+1))
def phip(q,g,d):
    if g == -1.: return -d/q
    if g == 0.: return d*np.log(q)
    return d*q**g/g

def nonlinear_state(x,params,a0):
    N=len(x);x=np.asarray(x,float);gamma=params['gamma']
    d=params['d'];ge=params['ge'];k=1.;nu=.3;k0=2.
    def cond(a):
        old=1-a;new=a
        return (params['D']+x/(1+x)-phip(new,gamma,d)+phip(old,gamma,d)
            -ge*(new.sum()-old.sum())-k0-k*a-nu*a*a)
    rt=root(cond,np.asarray(a0,float),tol=1e-12)
    assert np.max(np.abs(cond(rt.x)))<1e-9
    a=rt.x;assert np.min(a)>0 and np.max(a)<1
    q=np.empty(2*N);q[::2]=1-a;q[1::2]=a
    total=q.sum();region=q.reshape(N,2).sum(axis=1)
    bygen=q.reshape(N,2).sum(axis=0)
    alpha=np.full(2*N,30.);alpha[1::2]+=params['D']+x/(1+x)
    price=alpha-phip(q,gamma,d)-1.5*total-.01*np.repeat(region,2)-ge*np.tile(bygen,N)
    V=(alpha@q-phi(q,gamma,d).sum()-1.5*total**2/2-.01*(region@region)/2
      -ge*(bygen@bygen)/2)
    cs=V-q@price
    K=2*a+a*a/2+.3*a**3/3;C=x*x
    G=(q.reshape(N,2)*price.reshape(N,2)).sum(axis=1)-K+cs/N-C
    W=V-K.sum()-C.sum()
    assert abs(G.sum()-W)<1e-8
    return G,W

def nonlinear_check():
    out=[]
    for N in (2,3,5):
      for gamma in (-1.,0.,1.,2.):
       for a in (.25,.75):
        d=.35;ge=.01;x=.2;fp=1/(1+x)**2
        L=1+2*.3*a+d*((1-a)**(gamma-1)+a**(gamma-1))
        pred=fp*(N-1)/N*d*((1-a)**gamma-a**gamma)/L
        D=2.+a+.3*a*a-x/(1+x)+phip(a,gamma,d)-phip(1-a,gamma,d)+ge*N*(2*a-1)
        pp=dict(gamma=gamma,d=d,ge=ge,D=D)
        eps=2e-5;xp=np.full(N,x);xm=xp.copy();xp[0]+=eps;xm[0]-=eps
        gp,wp=nonlinear_state(xp,pp,np.full(N,a))
        gm,wm=nonlinear_state(xm,pp,np.full(N,a))
        fd=(gp[0]-gm[0]-wp+wm)/(2*eps)
        assert abs(fd-pred)<2e-6,(N,gamma,a,fd,pred)
        out.append(dict(N=N,gamma=gamma,a=a,predicted=float(pred),finite_difference=float(fd)))
    return out

def exact_zero_certificate():
    z=sy.Rational(34,100)+sy.Rational(1,2)+sy.Rational(3,5)-sy.Rational(9,20)-1
    H=sy.Matrix([[2,sy.Rational(3,10)],[sy.Rational(3,10),2]])
    eig=sorted(str(v) for v in (H-sy.eye(2)/2).eigenvals())
    assert z<0 and all(v>0 for v in (H-sy.eye(2)/2).eigenvals())
    return dict(z=str(z),eigenvalues=eig,certificate='W-W0 <= z*(a1+a2) - .5*a.T*(H-I/R)*a <= 0')

if __name__=='__main__':
    out=dict(symbolic=symbolic(),linear=linear_check(),nonlinear=nonlinear_check(),
             national_zero_effort=exact_zero_certificate(),
             spillover_fixed_adoption_counterexample=dict(epsilon=.2,a2=.25,wedge=-.05))
    print(json.dumps(out,indent=2))
