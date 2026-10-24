#!/usr/bin/env python3
"""Exact active-set enumeration of the unilateral research deviation at Delta=17/50.
SymPy; part of checkpoint 12. No claim of a Nash result throughout parameter interval.
"""
import itertools,json
import sympy as S
F=S.Rational
x=S.Symbol('x',real=True)
delta=F(17,50)
opp=F(389,6470)
e=F(3,10);d=2;z=delta-F(7,20)
H=S.Matrix([[d,e],[e,d]])
B=S.Matrix([[1,F(1,2),F(3,5),F(9,20)],
 [F(1,2),1,F(9,20),F(3,5)],
 [F(3,5),F(9,20),1,F(1,2)],
 [F(9,20),F(3,5),F(1,2),1]])
HMAX=F(5)
assert z+HMAX-d-abs(e)>0 and 2*HMAX>1
statuses=list(itertools.product([-1,0,1],repeat=2))
def resolve(status):
 free=[i for i,t in enumerate(status) if t==0]
 A=[F(0) if t==-1 else F(1) if t==1 else None for t in status]
 v=S.Matrix([z+x,z+opp])
 if free:
  Af=H.extract(free,free).inv()*S.Matrix(
   [v[i]-sum(H[i,j]*A[j] for j in range(2) if j not in free) for i in free])
  for i,w in zip(free,Af):A[i]=S.factor(w)
 a=S.Matrix(A)
 return a,S.simplify(v-H*a)
models={status:resolve(status) for status in statuses}
breaks={S.S.Zero,HMAX}
for status,(a,g) in models.items():
 for i,t in enumerate(status):
  eqs=[a[i],a[i]-1] if t==0 else [g[i]]
  for eq in eqs:
   if S.diff(eq,x)==0:continue
   r=S.solve(S.Eq(eq,0),x)
   if r and r[0].is_Rational and 0<r[0]<HMAX:breaks.add(r[0])
breaks=sorted(breaks)
def feasible(status,xx):
 a,g=models[status]
 for i,t in enumerate(status):
  v=S.factor(a[i].subs(x,xx));r=S.factor(g[i].subs(x,xx))
  if t==0 and not (0<=v<=1 and r==0):return False
  if t==-1 and not(v==0 and r<=0):return False
  if t==1 and not(v==1 and r>=0):return False
 return True
def payoff_poly(a):
 q=S.Matrix([1-a[0],a[0],1-a[1],a[1]])
 alpha=S.Matrix([10,10+delta+x,10,10+delta+opp])
 p=alpha-B*q
 Pi=(p[0]*q[0]+p[1]*q[1])-a[0]-a[0]**2/2
 CS=(q.T*B*q)[0]/2
 return S.factor(Pi+CS/2-x*x)
candidates=set(breaks);regimes=[]
for lo,hi in zip(breaks,breaks[1:]):
 mid=(lo+hi)/2
 valid=[st for st in statuses if feasible(st,mid)]
 assert len(valid)==1
 status=valid[0]
 v=payoff_poly(models[status][0])
 P=S.Poly(v,x)
 assert P.degree()==2
 A,B1,_=P.all_coeffs()
 if A<0:
  top=S.factor(-B1/(2*A))
  if lo<top<hi:candidates.add(top)
 regimes.append([str(lo),str(hi),str(status)])
def fullpay(xx):
 valid=[st for st in statuses if feasible(st,xx)]
 assert valid
 return S.factor(payoff_poly(models[valid[0]][0]).subs(x,xx))
values=sorted([(fullpay(t),t) for t in candidates],reverse=True)
assert values[0][1]==opp
assert sum(1 for u,t in values if u==values[0][0])==1
assert all(values[0][0]>u for u,t in values[1:])
result={'verified':True,'opponent_research':str(opp),
  'strict_unique_global_best_response':str(values[0][1]),
  'candidate_count':len(candidates),'distinct_regime_count':len(regimes),
  'second_best_candidate':{'x':str(values[1][1]),
    'payoff_gap':str(S.factor(values[0][0]-values[1][0]))},
  'beyond_x_5':'own conversion fixed at 1 and welfare derivative = 1-2*x < 0',
  'scope':'Delta=17/50 only. This is no claim of full-interval Nash or originality.'}
print(json.dumps(result,ensure_ascii=False,indent=2))
