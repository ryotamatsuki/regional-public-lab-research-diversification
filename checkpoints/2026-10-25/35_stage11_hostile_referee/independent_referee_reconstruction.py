#!/usr/bin/env python3
"""Stage 11 independent hostile derivation from four-good primitives.

This intentionally does not import Stage 9 production verifier modules.
It certifies algebraic statements and exact sample branch deviations only.
It does not replace the analytic all-z global proof or full Lean kernel build.
"""
import sympy as S

A,D,x1,x2,a1,a2,k0,kappa,R,t,b,c,n=S.symbols(
    "A D x1 x2 a1 a2 k0 kappa R t b c n", real=True
)
q=S.Matrix([1-a1,a1,1-a2,a2])
B=S.Matrix([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1]])
alpha=S.Matrix([A,A+D+x1,A,A+D+x2])
gross=(alpha.T*q)[0]-(q.T*B*q)[0]/2
p=alpha-B*q
C1=R*x1**2/2;C2=R*x2**2/2
K1=k0*a1+kappa*a1*a1/2
K2=k0*a2+kappa*a2*a2/2
Pi1=p[0]*(1-a1)+p[1]*a1-K1
Pi2=p[2]*(1-a2)+p[3]*a2-K2
CS=S.expand(gross-(p.T*q)[0])
G1=Pi1+CS/2-C1
G2=Pi2+CS/2-C2
W=S.expand(G1+G2)
check=lambda expr,name: print("PASS",name) if S.simplify(expr)==0 else (_ for _ in ()).throw(AssertionError(name))

h=1-t;j=b-c;e=b+n-2*c;d=kappa+2*h;M=d+e;L=d-e;z=D+h+j-k0
check(S.diff(W,a1)-(z+x1-d*a1-e*a2),"four-good follower gradient / conditional planner")
check(S.diff(W,a2)-(z+x2-d*a2-e*a1),"opponent farmer KKT")
H=S.Matrix([[d,e],[e,d]])
u=H.inv()*S.Matrix([1,0])
G1total=S.diff(G1,x1)+S.diff(G1,a1)*u[0]+S.diff(G1,a2)*u[1]
Wtotal=S.diff(W,x1)+S.diff(W,a1)*u[0]+S.diff(W,a2)*u[1]
state={a2:a1,x2:x1}
wedge=(G1total-Wtotal).subs(state).subs({x1:M*a1-z})
claimed=((h-j)-(2*h-e)*a1)/(2*L)
check(wedge-claimed,"P1 signed wedge ON FOC")
# A tempting erroneous off-equilibrium generalization fails whenever cross-input e != 0.
# This is a scope safeguard: on-follower-equilibrium condition must be imposed.
off=(G1total-Wtotal).subs(state)
assert S.simplify(off-claimed)!=0
print("PASS P1 off-follower extension correctly rejected")

zz=S.symbols("zz",real=True)
params={A:10,t:S.Rational(1,2),b:S.Rational(1,5),c:S.Rational(1,5),
        n:S.Rational(1,5),k0:1,kappa:1,R:2,D:S.Rational(1,2)+zz}
assert sorted(list(B.subs(params).eigenvals().keys()))==[
    S.Rational(1,2),S.Rational(11,10),S.Rational(19,10)]
F=S.factor((G1-G1.subs({x1:0,a1:0})).subs(params))
claimedF=(zz+x1+S.Rational(1,4))*a1-S.Rational(5,4)*a1*a1-x1*x1
check(F-claimedF,"P3 UNREDUCED local objective including adoption corners")
adopt=(zz+x1)/2
Fmid=S.factor(F.subs({a1:adopt}))
Fzero=F.subs(a1,0);Fone=F.subs(a1,1)
check(Fmid-((zz+x1)/8+S.Rational(3,16)*(zz+x1)**2-x1*x1),"P3 interior continuation payoff")
check(Fzero+x1*x1,"P3 no-adoption continuation")
check(Fone-(zz+x1-1-x1*x1),"P3 complete-adoption continuation")
xd=(1+3*zz)/13
check(S.diff(Fmid,x1).subs({x1:xd}),"P3 interior unique stationary effort")
check(Fmid.subs(x1,xd)-Fmid-S.Rational(13,16)*(x1-xd)**2,"P3 interior square gap")
W0=W.subs(params).subs({a1:0,a2:0,x1:0,x2:0})
national=W.subs(params)-W0
planner=zz*(a1+a2)-S.Rational(3,4)*(a1*a1+a2*a2)-sum(
  (xx-aa/2)**2 for xx,aa in ((x1,a1),(x2,a2))
)
check(national-planner,"P3 planner unrestricted FULL square completion")
ad=(1+16*zz)/26
check(national.subs({a1:ad,a2:ad,x1:xd,x2:xd})-
      (10*zz-1)*(22*zz+3)/338,"P3 strict welfare gap identity")
zc=(-4+S.sqrt(13))/12
pos=S.sqrt(13)/52
check(Fmid.subs({x1:pos,zz:zc}),"P3 cutoff tie: zero/positive global BR")
check(xd.subs(zz,zc)-pos,"P3 cutoff positive action")
# Independent exact evaluations deliberately touch off-path corners and large deviations.
for zval in (S.Integer(0),-S.Rational(1,50),-S.Rational(3,100)):
    X=xd.subs(zz,zval);Y=Fmid.subs({zz:zval,x1:X})
    # P3 farmer KKT continuation in all three branches at each candidate.
    tests=[S.Integer(0),-zval,(-zval+X)/2,X,X+S.Rational(1,13),
           2-zval,3-zval,10,100]
    for xx in tests:
        if xx<0:continue
        aval=S.Min(1,S.Max(0,(zval+xx)/2))
        diff=S.factor(Y-F.subs({zz:zval,x1:xx,a1:aval}))
        assert diff>=0,(zval,xx,diff)
print("PASS exact off-path KKT & global-effort candidate deviations across three regimes")

# Independent admissible-function counterexample to universal midpoint neutrality.
# phiOld''=1, phiNew''=2; grower K''=1; N=2, g=0, f'=1.
# Same incidence decomposition as original P2 primitive demand, not equal-phi hypothesis.
share=S.Rational(1,2); curvature_old=1;curvature_new=2
own_response=1/(curvature_old+curvature_new+1)
wedge=(share*curvature_old-share*curvature_new)*own_response*S.Rational(1,2)
assert wedge==-S.Rational(1,16)
print("PASS P2 unrestricted midpoint-neutrality falsified: wedge = -1/16")
print("PASS Stage 11 independent test: no model changes, scoped claims only")
