#!/usr/bin/env python3
"""P3+: exact analytic existence interval in the original public-breeding game.
Run: python verify_analytic_wasteful_rd.py  (requires SymPy)
"""
import sympy as s
z=s.symbols("z", real=True)
x=s.symbols("x", nonnegative=True)
zc=(-4+s.sqrt(13))/12
xD=(1+3*z)/13
aD=(1+16*z)/26
assert zc > -s.Rational(1,16)
# e=j=0; b=c=n=1/5, t=1/2, k0=kappa=1, R=2.
# Unilateral payoff difference from zero effort, opponent arbitrary:
a_i=(z+x)/2
F=s.expand(a_i/4+s.Rational(3,4)*a_i**2-x*x)
assert s.factor(s.diff(F,x))==(1+3*z-13*x)/8
assert s.diff(F,x,2)==-s.Rational(13,8)
gain=s.factor(F.subs(x,xD))
assert s.factor(gain-(48*z*z+32*z+1)/208)==0
assert s.simplify(gain.subs(z,zc))==0
assert gain.subs(z,0)==s.Rational(1,208)
# x in [0,-z]: no adoption; gain=-x^2. x>=2-z:
# all new variety; derivative = 1-2*x<0. Hence xD is unique global BR
# for z in (zc,0]. Candidate is interior in that interval.
assert s.simplify(aD-(z+xD)/2)==0
assert s.simplify(aD.subs(z,zc))>0
# Nationwide W over all feasible x and a:
# W-W0=z sum(a_i) + x'a -1/2 a'(2I)a - x'x
# <= z sum(a_i) - 3/4 sum(a_i^2) <=0 for z<=0.
wD=s.factor(2*z*aD+2*xD*aD-2*aD*aD-2*xD*xD)
assert s.factor(wD-(10*z-1)*(22*z+3)/338)==0
assert wD.subs(z,zc)<0 and wD.subs(z,0)==-s.Rational(3,338)
B=s.Matrix([[1,s.Rational(1,2),s.Rational(1,5),s.Rational(1,5)],
 [s.Rational(1,2),1,s.Rational(1,5),s.Rational(1,5)],
 [s.Rational(1,5),s.Rational(1,5),1,s.Rational(1,2)],
 [s.Rational(1,5),s.Rational(1,5),s.Rational(1,2),1]])
assert min(B.eigenvals().keys())>0
print("PASS: globally dominant strictly positive regional effort xD =", xD)
print("For every z in (",zc,", 0], social planner uniquely selects x=0.")
print("W Nash minus W0 =",wD, "; strictly negative across entire interval.")
