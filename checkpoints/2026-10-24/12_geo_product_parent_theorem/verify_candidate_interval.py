#!/usr/bin/env python3
"""Exact existing-baseline welfare counterpoint; does not certify original-source novelty."""
import json
import sympy as sp
D=sp.Symbol('Delta', real=True)
xD=(135*D-7)/647
ad=(680*D-203)/1294
xp=(20*D-7)/72
wD_minus_zero=sp.factor(sp.Rational(23,10)*ad**2-2*xD**2)
Delta_zero=sp.Rational(7,20)
Delta_conversion=sp.Rational(203,680)
assert sp.simplify(ad.subs(D,Delta_conversion))==0
assert Delta_conversion<sp.Rational(17,50)<Delta_zero
assert sp.simplify(xD.subs(D,sp.Rational(17,50))-sp.Rational(389,6470))==0
assert sp.simplify(ad.subs(D,sp.Rational(17,50))-sp.Rational(141,6470))==0
assert sp.simplify(wD_minus_zero.subs(D,sp.Rational(17,50))+sp.Rational(2569157,418609000))==0
assert wD_minus_zero.subs(D,Delta_conversion)<0
assert wD_minus_zero.subs(D,Delta_zero)<0
assert sp.simplify((xD-xp).subs(D,sp.Rational(5,4)))==0
Hminus=sp.Matrix([[sp.Rational(3,2),sp.Rational(3,10)],[sp.Rational(3,10),sp.Rational(3,2)]])
assert set(Hminus.eigenvals().keys())=={sp.Rational(6,5),sp.Rational(9,5)}
roots=sp.solve(wD_minus_zero,D)
assert roots[0]<Delta_conversion and roots[1]>Delta_zero
assert xD.subs(D,Delta_conversion)>0 and ad.subs(D,Delta_zero)>0
result={'all_symbolic_checks_passed':True,
        'candidate_adoption_interior_interval':['203/680','7/20'],
        'national_planner_zero_for_Delta_at_most':'7/20',
        'candidate_welfare_below_no_research_throughout_interval':True,
        'candidate_welfare_minus_no_research':str(wD_minus_zero),
        'Delta_0.34_best_response_requires_separate_active_set_certificate':True,
        'exact_delta_0.34_welfare_loss':str(wD_minus_zero.subs(D,sp.Rational(17,50))),
        'IMPORTANT':'This script does NOT claim global Nash throughout the interval; source-theorem nonabsorption remains UNRESOLVED.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
