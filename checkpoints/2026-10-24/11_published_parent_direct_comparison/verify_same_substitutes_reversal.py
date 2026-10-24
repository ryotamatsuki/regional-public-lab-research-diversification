#!/usr/bin/env python3
"""Stage 11 checkpoint (project numbering): mathematically audit sign-reversal
with unchanged strategic substitutes. Run: python verify_same_substitutes_reversal.py
Requires sympy. Does NOT validate existing literature novelty.
"""
import json
import sympy as s
h,j,e,k,R,z,Delta = s.symbols('h j e k R z Delta', real=True)
d=k+2*h
M=d+e
L=d-e
D=d*d-e*e
xi=(2*h-e)/(2*L)
astar=(h-j)/(2*h-e)
xd=s.factor(((1-xi)*z + M*(h-j)/(2*L))/(R*M-1+xi))
xp=s.factor(z/(R*M-1))
ap=R*xp
sub={h:s.Rational(1,2),j:s.Rational(3,20),e:s.Rational(3,10),k:1,R:2,z:Delta-s.Rational(7,20)}
xx=s.factor(xd.subs(sub))
pp=s.factor(xp.subs(sub))
aa=s.factor(ap.subs(sub))
cross=s.factor((-e/(2*D)).subs(sub))
assert s.simplify(xx - (135*Delta-7)/647)==0
assert s.simplify(pp - (20*Delta-7)/72)==0
assert s.simplify(aa - (20*Delta-7)/36)==0
assert cross == -s.Rational(15,391)
assert s.simplify(xd-xp-xi*M/(R*M-1+xi)*(astar-ap))==0
assert s.solve(s.Eq(aa,s.Rational(1,2)),Delta)==[s.Rational(5,4)]
rows=[]
for delta in [s.Rational(4,5),s.Rational(17,10)]:
    loc=s.factor(xx.subs(Delta,delta))
    pla=s.factor(pp.subs(Delta,delta))
    ad=s.factor(aa.subs(Delta,delta))
    rows.append({'Delta':str(delta),'cross_partial':str(cross),
        'local_effort':str(loc),'planner_effort':str(pla),
        'planner_adoption':str(ad),'effort_gap':str(loc-pla),
        'ranking':'over' if loc>pla else 'under'})
result={'symbolic_pass':True,'threshold_delta':'5/4','rows':rows,
    'scope':'Mathematics of the originally assumed interior two-region game. Literature nonabsorption UNRESOLVED; benchmark is national W, not producer-group cooperation.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
