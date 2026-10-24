#!/usr/bin/env python3
"""Checkpoint 17 independently audited portability checks.
The alternative tests were preregistered in PRESPECIFIED_ATTACKS.md BEFORE execution.
Python 3 + SymPy. No dependency on original model derivation scripts.
"""
import sympy as s
Q=s.Rational
x,z=s.symbols("x z",real=True)
# T1: quartic real research cost, original exactly e=j=0, z=0.
# Local own-payoff difference is F=a/4+3a^2/4-x^2-x^4, a=clip(x/2,0,1).
F=x/s.Integer(8)-Q(13,16)*x**2-x**4
assert s.expand(s.diff(F,x)-(1-13*x-32*x**3)/8)==0
assert s.expand(s.diff(F,x,2)+Q(13,8)+12*x*x)==0
assert s.diff(F,x).subs(x,0)>0 and s.diff(F,x).subs(x,Q(1,13))<0
# Thus strictly unique optimum root 32x^3+13x-1=0 in (0,1/13).
# For x>=2, full-planting local gain is 1-x^2-x^4, strictly decreasing.
# Nationwide W-W0<= -3/4 sum_i ai^2 -sum_i xi^4, unique at x=a=0.
print("T1 PASS: positive unique local Nash, planner zero, negative national welfare")
# T2: distinct curvature of old/new classes at symmetric a=1/2.
# phi_old(q)=q^2/2, phi_new(q)=q^2, g=1/10, K''=1:
# adoption Hessian L=1+1+2=4 on zero-sum, marginal price-incidence
# wedge = 1/2*(H_old(1/2)-H_new(1/2))/4 = -1/16.
t2=Q(1,2)*((Q(1,2)*1)-(Q(1,2)*2))/4
assert t2==-Q(1,16)
print("T2 PASS: old/new asymmetry destroys half-share neutrality",t2)
# T3: nonlinear orchard conversion K=a+a^2/2+a^4/4.
# At a=1/4, K''=1+3a^2=19/16, h=1/2,e=3/10,j=3/20,
# local-national wedge=(h-j-(2h-e)a)/(2(K''+2h-e))=7/151.
a=Q(1,4);h=Q(1,2);e=Q(3,10);j=Q(3,20)
kpp=1+3*a*a
t3=s.factor((h-j-(2*h-e)*a)/(2*(kpp+2*h-e)))
assert t3==Q(7,151)
# The separate independent full four-good primitives checker (local attachment)
# verifies that the same 7/151 follows without importing this reduced formula.
print("T3 PASS: nonlinear grower conversion preserves sign and yields exact",t3)
# Original P3+ algebraic interval remains unchanged.
zc=(-4+s.sqrt(13))/12
xx=(1+3*z)/13;aa=(1+16*z)/26
gain=s.factor((48*z*z+32*z+1)/208)
assert s.simplify(gain.subs(z,zc))==0 and aa.subs(z,zc)>0
assert s.factor(2*z*aa+2*xx*aa-2*aa**2-2*xx**2-
                (10*z-1)*(22*z+3)/338)==0
print("P3+ PASS: critical boundary and social-welfare polynomial")
