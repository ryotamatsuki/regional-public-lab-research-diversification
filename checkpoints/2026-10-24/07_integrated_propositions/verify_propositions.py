"""Stage 07 integrated proposition verifier.

Run from any directory:
    python checkpoints/2026-10-24/07_integrated_propositions/verify_propositions.py

Requirements: sympy, numpy, scipy.  Reuses the archived Stage 04 exact
active-set enumerator for the 3 rational global Nash certificates; algebraic
proof tests here are separately reconstructed from Stage 06.
"""
import importlib.util
import json
from pathlib import Path
from fractions import Fraction as F
import sympy as s

# Independent SymPy identities for the linear model.
h,j,e,k,R,z,x,y,A,b=s.symbols("h j e k R z x y A b",real=True)
d=k+2*h; M=d+e; L=d-e; D=d*d-e*e
ai=z/M+(d*x-e*y)/D
aj=z/M+(d*y-e*x)/D
cs=1+b-(h+j)*(ai+aj)+h*(ai**2+aj**2)+e*ai*aj
Gi=A-1-b+h*ai+j*aj+k*ai**2/2+cs/2-R*x**2/2
Gj=A-1-b+h*aj+j*ai+k*aj**2/2+cs/2-R*y**2/2
W=2*A-1-b+d*(ai**2+aj**2)/2+e*ai*aj-R*(x*x+y*y)/2
xi=(2*h-e)/(2*L)
eta=((2*k+2*h-e)*z/M+h-j)/(2*L)
xd=((1-xi)*z+M*(h-j)/(2*L))/(R*M-1+xi)
xp=z/(R*M-1)
tests={
    "welfare_aggregation":Gi+Gj-W,
    "regional_best_response_FOC":s.diff(Gi,x)-(eta-(R-(h+k)/D)*x-e*y/(2*D)),
    "strategic_cross_partial":s.diff(Gi,x,y)+e/(2*D),
    "planner_envelope":s.diff(W,x)-(ai-R*x),
    "symmetric_wedge":(s.diff(Gi,x)-s.diff(W,x)-(h-j-(2*h-e)*(z+x)/M)/(2*L)).subs(y,x),
    "effort_ranking":xd-xp-xi*M*((h-j)/(2*h-e)-R*xp)/(R*M-1+xi),
    "interior_welfare_gap":(
        ((z+xp)**2-(z+xd)**2)/M-R*(xp**2-xd**2)
        -(R-1/M)*(xd-xp)**2)
}
for label,val in tests.items():
    assert s.simplify(val)==0,(label,s.factor(val))

# Preserve and explicitly cite original globally exhaustive piecewise method.
stage04=Path(__file__).resolve().parents[1]/"04_varietal_replacement"/"verify_breeding.py"
spec=importlib.util.spec_from_file_location("archived_breeding",stage04)
mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
results=[]
for delta in (F(4,5),F(17,10),F(17,50)):
    P=mod.linear_parameters(delta)
    xD=(135*delta-7)/647
    aD=(680*delta-203)/1294
    xP=max(F(0),(20*delta-7)/72)
    aP=max(F(0),(20*delta-7)/36)
    local=mod.linear_state([xD,xD],P)
    planner=mod.linear_state([xP,xP],P)
    assert local["a"]==[aD,aD]
    assert planner["a"]==[aP,aP]
    br,br_value,n_candidates=mod.exact_best_response(xD,P)
    assert br==xD and br_value==local["G"][0]
    assert planner["W"]>=local["W"]
    results.append(dict(Delta=str(delta),xN=str(xD),aN=str(aD),
       xP=str(xP),aP=str(aP),global_BR=str(br),
       candidate_count=n_candidates,
       welfare_gap=str(planner["W"]-local["W"])))
assert (F(17,50)+F(1,2)+F(3,20)-1)==-F(1,100)
assert F(17,10)-F(1,2)==F(6,5)
assert F(23,10)-F(1,2)==F(9,5)
print(json.dumps({"symbolic_identities":list(tests),
                  "global_exact_examples":results,
                  "planner_zero_effort_certificate":{"z":"-1/100",
                      "eigenvalues_H_minus_I_over_R":["6/5","9/5"]},
                  "scope":"nonlinear Proposition 2 is analytic and has separate Stage04 finite-difference checks"},indent=2))
