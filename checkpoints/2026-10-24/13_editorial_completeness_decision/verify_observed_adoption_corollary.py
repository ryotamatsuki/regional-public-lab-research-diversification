#!/usr/bin/env python3
"""Independent Stage-13-checkpoint audit: the observed-decentralized-adoption
policy sign is a COROLLARY of existing P1, not a novel fourth proposition.
Run with SymPy; original baseline model unchanged.
"""
import sympy as s
h,j,e,k,R,z=s.symbols('h j e k R z',real=True)
L=k+2*h-e;M=k+2*h+e
xi=(2*h-e)/(2*L)
a_star=(h-j)/(2*h-e)
xD=s.factor(((1-xi)*z+M*(h-j)/(2*L))/(R*M-1+xi))
aD=s.factor((z+xD)/M)
xP=s.factor(z/(R*M-1))
aP=s.factor(R*xP)
# At an interior symmetric Nash, G_i' = 0, so W_i' = -[G_i'-W_i'].
assert s.factor((aD-R*xD)+xi*(a_star-aD))==0
# Under strict interior and RM>1, both shares are on the same side of a_star.
assert s.factor((aD-a_star)-(R*M-1)/(R*M-1+xi)*(aP-a_star))==0
assert s.factor((xD-xP)-xi*M/(R*M-1+xi)*(a_star-aP))==0
p={h:s.Rational(1,2),j:s.Rational(3,20),e:s.Rational(3,10),k:s.Integer(1),R:s.Integer(2)}
for Delta in [s.Rational(4,5),s.Rational(17,10),s.Rational(17,50)]:
    zz=Delta-s.Rational(7,20)
    w=s.factor((aD-R*xD).subs({**p,z:zz}))
    print('Delta =',Delta,'a_D =',aD.subs({**p,z:zz}),'W_i at Nash =',w)
print('PASS: 3 exact symbolic identities. At Delta=0.34 the planner is a CORNER, so its interior formula is not the optimum.')
