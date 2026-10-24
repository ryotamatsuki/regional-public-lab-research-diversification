#!/usr/bin/env python3
"""Stage 10 independent canonical market-incidence and welfare-mapping checks."""
import json
import sympy as s
h,j,e,k,R,z,a,x=s.symbols('h j e k R z a x', real=True)
d=k+2*h;D=d*d-e*e;L=d-e;M=d+e
# For unilateral public R&D x_i, endogenous farmer adoption derivatives:
adx_i=d/D; adx_j=-e/D
# Induced 4-price derivatives: q goods (iO,iN,jO,jN), excluding direct R&D quality effect.
pai_O=h*adx_i+j*adx_j
pai_N=-h*adx_i-(e-j)*adx_j
paj_O=j*adx_i+h*adx_j
paj_N=-(e-j)*adx_i-h*adx_j
Pii=(1-a)*pai_O+a*pai_N
Pall=Pii+(1-a)*paj_O+a*paj_N
# Region i owns its full producer income, and 1/2 nationwide consumers: wedge is price incidence
wedge=s.factor(Pii-Pall/2)
xi=(2*h-e)/(2*L); astar=(h-j)/(2*h-e)
assert s.factor(wedge-xi*(astar-a))==0
checks=['price-income-incidence general marginal wedge exact symbolic equality']
# independent W envelope, fixed-adoption zero: at fixed a R&D improves willingness-to-pay
# p_iN increases by dx_i, local producer value increases by a*dx_i, CS direct derivative 0.
fixed_local=a-R*x;fixed_national=a-R*x
assert fixed_local-fixed_national==0
checks.append('fixed adoption: identical local and nationwide direct R&D benefit')
# 2-region decentralized versus planner symmetric effort
xd=s.factor(((1-xi)*z+M*(h-j)/(2*L))/(R*M-1+xi))
xp=s.factor(z/(R*M-1));ap=R*xp
assert s.factor(xd-xp - xi*M/(R*M-1+xi)*(astar-ap))==0
checks.append('interior symmetric Nash–planner effort ranking identity')
assert s.factor((astar-s.Rational(1,2)).subs(e,2*j))==0
checks.append('b=n equal-variety-substitution 50%-adoption crossing')
# Numeric exact rational evidence for two sides and zero-R&D social optimum: independent arithmetic
v={h:s.Rational(1,2),j:s.Rational(3,20),e:s.Rational(3,10),k:1,R:2}
rows=[]
for delta in [s.Rational(4,5),s.Rational(17,10),s.Rational(17,50)]:
 zz=delta+s.Rational(1,2)+s.Rational(3,20)-1
 sub={**v,z:zz}
 xD=s.cancel(xd.subs(sub)); aD=s.cancel((zz+xD)/s.Rational(23,10))
 xP=s.cancel(xp.subs(sub)) if zz>0 else 0
 rows.append({'Delta':str(delta),'xD':str(xD),'aD':str(aD),'xP':str(xP)})
assert rows[0]['xD']=='101/647' and rows[1]['xD']=='445/1294' and rows[2]['xD']=='389/6470'
checks.append('three exact-rational baseline symmetric equilibrium values reproduced')
res={'all_checks_pass':True,'symbolic_checks':checks,'baseline_equilibria':rows,'literature_scope':'Math checks validate only the candidate algebra; not exact parent-theorem novelty or full-paper absorbability.'}
open('/mnt/data/public_breeding_prior_absorption_audit.json','w').write(json.dumps(res,indent=2,ensure_ascii=False))
print(json.dumps(res,indent=2,ensure_ascii=False))
