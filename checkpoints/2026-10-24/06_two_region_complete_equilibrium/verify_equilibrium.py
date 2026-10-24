#!/usr/bin/env python3
"""Stage 06: independently recompute two-region prices and welfare.
Python 3; numpy, scipy, sympy. Command: python verify_equilibrium.py
"""
import json
import numpy as np
import sympy as sp
from scipy.optimize import minimize, minimize_scalar
A,t,b,n,c,k0,k,R=10.,.5,.6,.6,.45,1.,1.,2.
h=1-t;j=b-c;e=b+n-2*c;d=k+2*h;M=d+e;L=d-e;D=d*d-e*e
B=np.array([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1.]])
S=np.array([[-1.,0.],[1.,0.],[0.,-1.],[0.,1.]])
H=np.array([[d,e],[e,d]])

def state(delta,x,adoption=None):
    x=np.asarray(x,dtype=float)
    z=delta+h+j-k0
    rhs=np.array([z+x[0],z+x[1]])
    if adoption is None:
        trial=np.linalg.solve(H,rhs)
        if np.min(trial)>=0 and np.max(trial)<=1:
            a=trial
        else:
            sol=minimize(lambda v:.5*v@H@v-rhs@v,
                np.clip(trial,0,1),jac=lambda v:H@v-rhs,
                bounds=[(0.,1.)]*2,method="L-BFGS-B",
                options={"ftol":1e-14})
            assert sol.success
            a=sol.x
    else:
        a=np.asarray(adoption,dtype=float)
    q=np.array([1-a[0],a[0],1-a[1],a[1]])
    alpha=np.array([A,A+delta+x[0],A,A+delta+x[1]])
    prices=alpha-B@q
    V=alpha@q-.5*q@B@q
    cs=V-prices@q
    K=k0*a+.5*k*a*a
    Pi=np.array([q[:2]@prices[:2],q[2:]@prices[2:]])-K
    G=Pi+cs/2-R*x*x/2
    W=G.sum()
    assert abs(W-(V-K.sum()-R*x@x/2))<1e-10
    return {"x":x,"a":a,"p":prices,"Pi":Pi,"CS":cs,"G":G,"W":W}

def sympy_audit():
    zz,xx,yy,kk,hh,ee,jj,rr,aa,bb=sp.symbols("z x y k h e j R A b")
    dd=kk+2*hh; MM=dd+ee; DD=dd**2-ee**2; LL=dd-ee
    ai=zz/MM+(dd*xx-ee*yy)/DD
    aj=zz/MM+(dd*yy-ee*xx)/DD
    CS=1+bb-(hh+jj)*(ai+aj)+hh*(ai**2+aj**2)+ee*ai*aj
    G=aa-1-bb+hh*ai+jj*aj+kk*ai**2/2+CS/2-rr*xx**2/2
    Gother=aa-1-bb+hh*aj+jj*ai+kk*aj**2/2+CS/2-rr*yy**2/2
    eta=((2*kk+2*hh-ee)*zz/MM+hh-jj)/(2*LL)
    foc=eta-(rr-(hh+kk)/DD)*xx-ee*yy/(2*DD)
    W=2*aa-1-bb+dd*(ai**2+aj**2)/2+ee*ai*aj-rr*(xx**2+yy**2)/2
    assert sp.simplify(sp.diff(G,xx)-foc)==0
    assert sp.simplify(sp.diff(G,yy,xx)+ee/(2*DD))==0
    assert sp.simplify(G+Gother-W)==0
    assert sp.simplify(sp.diff(W,xx)-(ai-rr*xx))==0
    return "PASS: FOC, strategic cross partial, regional aggregation, planner envelope"

def compute():
    results=[]
    for delta in [0.8,1.7,0.34]:
        xd=(135*delta-7)/647
        aD=(680*delta-203)/1294
        decentralized=state(delta,[xd,xd])
        assert abs(decentralized["a"][0]-aD)<1e-10
        # Global constrained planner over the jointly strictly concave (x,a) objective.
        z=delta+h+j-k0
        def joint(v):
            x=v[:2];a=v[2:]
            return 2*A-1-b+z*a.sum()+x@a-.5*a@H@a-R*x@x/2
        sol=minimize(lambda v:-joint(v),np.zeros(4),method="SLSQP",
            bounds=[(0,5)]*2+[(0,1)]*2,
            options={"ftol":1e-14,"maxiter":500})
        assert sol.success
        planner=state(delta,sol.x[:2])
        assert np.max(abs(planner["a"]-sol.x[2:]))<1e-6
        # Globally scan unilateral deviation on [0,5] and refine its local peak.
        objective=lambda u: state(delta,[u,xd])["G"][0]
        xx=np.linspace(0,5,1001)
        best_index=max(range(len(xx)),key=lambda idx:objective(xx[idx]))
        lo=xx[max(best_index-1,0)]
        hi=xx[min(best_index+1,len(xx)-1)]
        best=minimize_scalar(lambda u:-objective(u),
            bounds=(lo,hi),method="bounded",
            options={"xatol":1e-12})
        assert abs(best.x-xd)<1e-5,(delta,xd,best.x)
        for label,v in [("Nash",decentralized),("Planner",planner)]:
            row=dict(Delta=delta,solution=label,x=float(v["x"][0]),
                a=float(v["a"][0]),pOld=float(v["p"][0]),pNew=float(v["p"][1]),
                Pi=float(v["Pi"][0]),CS=float(v["CS"]),
                G=float(v["G"][0]),W=float(v["W"]))
            results.append(row)
    assert np.min(np.linalg.eigvalsh(B))>0
    assert np.min(np.linalg.eigvalsh(R*H-np.eye(2)))>0
    return results

if __name__=="__main__":
    result={"sympy":sympy_audit(),"results":compute(),
        "scope":"All closed forms require interior adoption; numerical unilateral global screen limited to x in [0,5]; Stage04 contains exact piecewise best-response checks."}
    print(json.dumps(result,indent=2))
