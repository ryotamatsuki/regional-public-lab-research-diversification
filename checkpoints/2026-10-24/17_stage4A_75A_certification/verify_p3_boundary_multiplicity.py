#!/usr/bin/env python3
"""Exact P3+ lower boundary: degeneracy and multiple research Nash equilibria."""
import sympy as s
zc=(-4+s.sqrt(13))/12
positive_research=s.factor((1+3*zc)/13)
assert s.simplify(positive_research-s.sqrt(13)/52)==0
assert zc<0 and positive_research > -zc and positive_research<2-zc
adoption=s.factor((zc+positive_research)/2)
assert adoption>0 and adoption<1
# Branch objective for z+x>0 and z+x<2:
x=s.symbols("x",real=True)
F=s.expand((zc+x)/8+s.Rational(3,16)*(zc+x)**2-x*x)
assert s.diff(F,x,2)==-s.Rational(13,8)
assert s.simplify(F.subs(x,positive_research))==0
assert s.simplify(s.diff(F,x).subs(x,positive_research))==0
# At x=0 with zc<0, adoption is 0, payoff change is 0, not F(0).
# For 0<x<=-zc, payoff -x²<0. For interior branch strict
# concavity gives F<=F(positive_research)=0. For x>=2-zc,
# derivative 1-2x<0. Both 0 and positive_research globally maximize.
# e=j=0 makes the two local best responses independent:
# exactly 2x2=4 pure research Nash profiles at zc.
print("PASS lower boundary: BR set =",[0,str(positive_research)])
print("Exactly four pure research Nash profiles at the excluded z=zc endpoint.")
