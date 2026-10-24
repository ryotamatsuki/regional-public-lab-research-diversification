#!/usr/bin/env python3
"""Exact 9-regime globally optimal unilateral research deviation at e=1/100.
Original 4-good regional public-breeding model; exact SymPy rational algebra.
Run: python verify_positive_e_global_nash.py
"""
import itertools
import sympy as S
F=S.Rational
x=S.Symbol("x", real=True)
delta=F(49,100);z=delta-F(1,2);e=F(1,100);d=2
h=F(1,2);j=F(0);R=2;kappa=1
L=d-e;M=d+e;xi=(2*h-e)/(2*L)
opp=S.factor(((1-xi)*z+M*(h-j)/(2*L))/(R*M-1+xi))
B=S.Matrix([[1,F(1,2),F(1,5),F(1,5)],
 [F(1,2),1,F(1,5),F(21,100)],
 [F(1,5),F(1,5),1,F(1,2)],
 [F(1,5),F(21,100),F(1,2),1]])
H=S.Matrix([[d,e],[e,d]])
assert min(B.eigenvals().keys())>0
assert z==-F(1,100)
assert -e/(2*(d*d-e*e))==-F(50,39999)<0
MAX=F(5)
# Saturation beyond MAX gives marginal local payoff 1-2*x<0.
assert z+MAX-d-abs(e)>0 and 2*MAX>1
statuses=list(itertools.product([-1,0,1],repeat=2))
def regime(st):
 free=[i for i,t in enumerate(st) if t==0]
 v=S.Matrix([z+x,z+opp])
 a=[F(0) if t==-1 else F(1) if t==1 else None for t in st]
 if free:
  af=H.extract(free,free).inv()*S.Matrix(
    [v[i]-sum(H[i,j]*a[j] for j in range(2) if j not in free) for i in free])
  for i,value in zip(free,af):a[i]=S.factor(value)
 a=S.Matrix(a)
 return a,S.simplify(v-H*a)
regimes={st:regime(st) for st in statuses}
breaks={S.S.Zero,MAX}
for st,(a,g) in regimes.items():
 for i,t in enumerate(st):
  exprs=[a[i],a[i]-1] if t==0 else [g[i]]
  for expression in exprs:
   if S.diff(expression,x)==0:continue
   roots=S.solve(S.Eq(expression,0),x)
   if roots and roots[0].is_Rational and 0<roots[0]<MAX:breaks.add(roots[0])
breaks=sorted(breaks)
def feasible(st,xx):
 a,g=regimes[st]
 for i,t in enumerate(st):
  ai=S.factor(a[i].subs(x,xx));r=S.factor(g[i].subs(x,xx))
  if t==0 and not (0<=ai<=1 and r==0):return False
  if t==-1 and not (ai==0 and r<=0):return False
  if t==1 and not (ai==1 and r>=0):return False
 return True
def G(a):
 q=S.Matrix([1-a[0],a[0],1-a[1],a[1]])
 alpha=S.Matrix([10,10+delta+x,10,10+delta+opp])
 p=alpha-B*q
 pi=p[0]*q[0]+p[1]*q[1]-a[0]-a[0]*a[0]/2
 cs=(q.T*B*q)[0]/2
 return S.factor(pi+cs/2-x*x)
candidates=set(breaks)
nonempty=0
for lo,hi in zip(breaks,breaks[1:]):
 st=[u for u in statuses if feasible(u,(lo+hi)/2)]
 assert len(st)==1,(lo,hi,st)
 P=S.Poly(G(regimes[st[0]][0]),x)
 assert P.degree()==2
 A1,B1,_=P.all_coeffs()
 if A1<0:
  v=S.factor(-B1/(2*A1))
  if lo<v<hi:candidates.add(v)
 nonempty+=1
def payoff(xx):
 valid=[st for st in statuses if feasible(st,xx)]
 assert valid
 return S.factor(G(regimes[valid[0]][0]).subs(x,xx))
ranking=sorted([(payoff(t),t) for t in candidates],reverse=True)
assert ranking[0][1]==opp
assert all(ranking[0][0]>v for v,t in ranking[1:])
ad=S.factor((z+opp)/M)
assert 0<ad<1
Wdiff=S.factor(2*z*ad+2*opp*ad-M*ad*ad-2*opp*opp)
assert Wdiff<0
# Planner global zero: z<0; H-(1/R)*I positive definite.
assert min((H-S.eye(2)/R).eigenvals().keys())>0
print('PASS:',len(candidates),'global BR candidates,',nonempty,'regimes; exact xD',opp,'aD',ad)
print('Cross R&D partial',-e/(2*(d*d-e*e)),'W_D-W0',Wdiff)
print('Next closest candidate',ranking[1][1],'strict local payoff margin',S.factor(ranking[0][0]-ranking[1][0]))
print('No claim of unique Nash among asymmetric profiles or generalized full-parameter sign.')
