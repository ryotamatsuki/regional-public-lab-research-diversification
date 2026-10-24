#!/usr/bin/env python3
"""Independent primitive-level Stage 11 hostile checks, exact SymPy arithmetic.

This is NOT a Lean kernel proof, Nash active-set exhaustive test, or
independent editor's novelty opinion. It deliberately rebuilds producer
receipts, CS and regional welfare from the original four-good primitive.
"""
import sympy as s

A, Delta, t, b, c, n, k0, kappa, R = s.symbols(
    "A Delta t b c n k0 kappa R", real=True
)
x1,x2,a1,a2 = s.symbols("x1 x2 a1 a2",real=True)
q=s.Matrix([1-a1,a1,1-a2,a2])
alpha=s.Matrix([A,A+Delta+x1,A,A+Delta+x2])
B=s.Matrix([[1,t,b,c],[t,1,c,n],[b,c,1,t],[c,n,t,1]])
V=s.expand(alpha.dot(q)-(q.T*B*q)[0]/2)
p=alpha-B*q
CS=s.expand(V-p.dot(q))
def real_conversion(a):
    return k0*a+kappa*a**2/2
Pi1=s.expand(p[0]*(1-a1)+p[1]*a1-real_conversion(a1))
Pi2=s.expand(p[2]*(1-a2)+p[3]*a2-real_conversion(a2))
G1=Pi1+CS/2-R*x1*x1/2
W=Pi1+Pi2+CS-R*(x1*x1+x2*x2)/2
h=1-t
j=b-c
e=b+n-2*c
d=kappa+2*h
M=d+e
L=d-e
z=Delta+h+j-k0
D=d*d-e*e
assert s.factor(p[1]-p[0]-(k0+kappa*a1)-(z+x1-d*a1-e*a2))==0

# Follower responds to x1 with derivative (d,-e)/(d²-e²).
G1_total=s.diff(G1,x1)+s.diff(G1,a1)*d/D-s.diff(G1,a2)*e/D
W_total=s.diff(W,x1)+s.diff(W,a1)*d/D-s.diff(W,a2)*e/D
a,x=s.symbols("a x",real=True)
symmetric={a1:a,a2:a,x1:x,x2:x}
candidate=(2*h-e)/(2*L)*((h-j)/(2*h-e)-a)
assert s.factor(s.together((G1_total-W_total).subs(symmetric)-candidate).subs(x,M*a-z))==0

# P3 exact family; use off-equilibrium primitive G rather than FOC shortcut.
zz=s.Symbol("zz",real=True)
params={t:s.Rational(1,2),b:s.Rational(1,5),c:s.Rational(1,5),
        n:s.Rational(1,5),k0:1,kappa:1,R:2,
        Delta:s.Rational(1,2)+zz}
Gp3=s.expand(G1.subs(params))
Wp3=s.expand(W.subs(params))
regional=s.factor(Gp3-Gp3.subs({a1:0,x1:0}))
social=s.factor(Wp3-Wp3.subs({a1:0,a2:0,x1:0,x2:0}))
assert s.expand(regional-((zz+x1+s.Rational(1,4))*a1-s.Rational(5,4)*a1**2-x1**2))==0
assert s.expand(social-(zz*(a1+a2)+x1*a1+x2*a2-a1**2-a2**2-x1**2-x2**2))==0
assert s.expand(regional.subs(a1,1)-(zz+x1-1-x1**2))==0

mid=s.factor(regional.subs(a1,(zz+x1)/2))
opt=(1+3*zz)/13
adopt=(1+16*zz)/26
assert s.simplify(s.diff(mid,x1).subs(x1,opt))==0
assert s.factor(mid.subs(x1,opt)-mid-s.Rational(13,16)*(x1-opt)**2)==0
assert s.factor(mid.subs(x1,opt)-(48*zz**2+32*zz+1)/208)==0
w_at=s.factor(social.subs({x1:opt,x2:opt,a1:adopt,a2:adopt}))
assert s.factor(w_at-(10*zz-1)*(22*zz+3)/338)==0
# Separate unilateral improvement from mutual-restraint gains: the rival's
# consumer-surplus contribution cancels in a unilateral but not joint baseline.
mutual={x1:opt,x2:opt,a1:adopt,a2:adopt}
zero={x1:0,x2:0,a1:0,a2:0}
other_stays={x1:0,x2:opt,a1:0,a2:adopt}
g_local_joint=s.factor(Gp3.subs(mutual)-Gp3.subs(zero))
g_local_unilateral=s.factor(Gp3.subs(mutual)-Gp3.subs(other_stays))
assert s.factor(g_local_joint-w_at/2)==0
assert s.factor(g_local_unilateral-(48*zz**2+32*zz+1)/208)==0
assert g_local_joint.subs(zz,0)==-s.Rational(3,676)
assert g_local_unilateral.subs(zz,0)==s.Rational(1,208)
square=zz*(a1+a2)-s.Rational(3,4)*(a1*a1+a2*a2)-(x1-a1/2)**2-(x2-a2/2)**2
assert s.expand(social-square)==0
zc=(-4+s.sqrt(13))/12
assert s.simplify(48*zc**2+32*zc+1)==0
assert s.simplify(opt.subs(zz,zc)-s.sqrt(13)/52)==0

B0=B.subs(params)
assert B0.eigenvals()=={s.Rational(19,10):1,s.Rational(11,10):1,s.Rational(1,2):2}
print("PASS: four-good competitive KKT from prices, P1 incidence wedge, "
      "off-equilibrium full-adoption regional payoff, P3 global proof identities, "
      "all B eigenvalues positive, welfare loss, and exact endpoint threshold.")
print("IMPORTANT: global best response and all asymmetric Nash remain separate proof obligations.")
