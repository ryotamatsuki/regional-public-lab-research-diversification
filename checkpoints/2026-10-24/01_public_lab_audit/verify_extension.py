"""Exact checks for the proposed selective-capacity extension, not a novelty test."""
from model_check import market, stats, R
import sympy as s
import json
from pathlib import Path

OUT=Path(__file__).parent / 'results.json'
a,b,V,RR,H=stats()
fee=R(1,20)
pL,pH=R(3,20),R(3,10)
cost=R(61,10000)
da=a['A']-a['B']
rA=(a['A']+b['A']+fee)/2
rB=(a['B']+b['B']+fee)/2
assert 0<fee<min(a[r]-b[r] for r in ['A','B'])
assert rA>RR['BA'] and rB>RR['AB'] and da>0
t=s.factor(da/(rA-RR['BA']))
assert pL<t<pH

def h(pi,pj,rho):
    return rho*min(pi,pj)+(1-rho)*pi*pj
def margins(pi,pj,rs=R(0),rd=R(0)):
    return [s.factor(pi*da-h(pi,pj,rs)*rA+h(pi,pj,rd)*RR['BA']),
            s.factor(pi*da-h(pi,pj,rd)*RR['AB']+h(pi,pj,rs)*rB)]
def equilibria(p1,p2,rs=R(0),rd=R(0)):
    ans=[]
    m1=margins(p1,p2,rs,rd);m2=margins(p2,p1,rs,rd)
    for x in ['A','B']:
        for y in ['A','B']:
            u=m1[0 if y=='A' else 1];v=m2[0 if x=='A' else 1]
            if (u>0 if x=='A' else u<0) and (v>0 if y=='A' else v<0):ans.append(x+y)
    return ans

assert equilibria(pL,pL)==['AA']
assert equilibria(pH,pL)==['AB']
assert equilibria(pL,pH)==['BA']
assert equilibria(pH,pH)==['AB','BA']
# A is strictly dominant for the strengthened lab, ruling out every mixed equilibrium.
assert all(x>0 for x in margins(pH,pL))
assert margins(pL,pH)[0]<0<margins(pL,pH)[1]

# Even the largest accepted direction-specific fee cannot make B a best response
# to A at low-low capacities within the anonymous random-priority/fallback class.
best_possible_A_overlap=a['A']
low_max_B_obedience=s.factor(-pL*da+pL*pL*(best_possible_A_overlap-RR['BA']))
assert low_max_B_obedience<0
min_A_against_B=pL*(da+pL*((a['B']+b['B'])/2-RR['AB']))
assert min_A_against_B>0

def welfare(p1,p2,x,y,rs=R(0),rd=R(0)):
    if x==y:return (p1+p2-h(p1,p2,rs))*V[x]
    return p1*V[x]+p2*V[y]-h(p1,p2,rd)*H[x+y]

w0=welfare(pL,pL,'A','A')
w1=welfare(pH,pL,'A','B')-cost
w2_upper=max(welfare(pH,pH,x,y) for x in ['A','B'] for y in ['A','B'])-2*cost
direct=s.factor(welfare(pH,pL,'A','A')-w0-cost)
total=s.factor(w1-w0)
assert direct<0<total and w2_upper<w0<w1
assert V['A']==R(233,5000) and V['B']==R(311827,7744000)

# Exact market regularity, including all principal minors (positive definiteness).
for x in [None,'A','B']:
    for y in [None,'A','B']:
        m=market(x,y)
        assert min(m['q'])>0 and min(m['prices'])>0
# Demand and FOC matrices reconstructed separately for definiteness checks.
for x in [None,'A','B']:
    for y in [None,'A','B']:
        kinds=['old','old']; own=[0,1]
        for i,r in enumerate([x,y]):
            if r:kinds.append(r);own.append(i)
        n=len(kinds);M=s.eye(n)
        for j in range(n):
            for k in range(j):M[j,k]=M[k,j]=R(3,4) if kinds[j]==kinds[k] and kinds[j]!='old' else R(1,2)
        Q=s.Matrix(n,n,lambda j,k:2*M[j,k] if own[j]==own[k] else M[j,k])
        assert all(M[:j,:j].det()>0 and Q[:j,:j].det()>0 for j in range(1,n+1))

rs,rd=R(1,500),R(1,1000)
assert equilibria(pL,pL,rs,rd)==['AA']
assert equilibria(pH,pL,rs,rd)==['AB']
assert all(x>0 for x in margins(pH,pL,rs,rd))
w0c=welfare(pL,pL,'A','A',rs,rd)
directc=s.factor(welfare(pH,pL,'A','A',rs,rd)-w0c-cost)
totalc=s.factor(welfare(pH,pL,'A','B',rs,rd)-cost-w0c)
twoc=max(welfare(pH,pH,x,y,rs,rd) for x in ['A','B'] for y in ['A','B'])-2*cost
assert directc<0<totalc and twoc<w0c

def enc(obj):
    if isinstance(obj,dict):return {k:enc(v) for k,v in obj.items()}
    if isinstance(obj,(tuple,list)):return [enc(x) for x in obj]
    if isinstance(obj,str):return obj
    return {'exact':str(obj),'decimal':float(obj)}

data=enc(dict(status='PASS',alpha=a,beta=b,V=V,local_overlap=RR,national_overlap=H,
    fee=fee,capacity_cost=cost,low_probability=pL,high_probability=pH,
    threshold=t,best_possible_fee_threshold=s.factor(da/(a['A']-RR['BA'])),
    social_direction_threshold=s.factor((V['A']-V['B'])/(V['A']-H['AB'])),
    low_max_B_obedience=low_max_B_obedience,
    low_margins=margins(pL,pL),high_lab_margins=margins(pH,pL),low_against_high_margins=margins(pL,pH),
    welfare_no_upgrade=w0,welfare_one_upgrade=w1,welfare_two_upgrades_upper_bound=w2_upper,
    direct_capacity_gain_net=direct,total_policy_gain_net=total,
    direction_change_gain=s.factor(total-direct),
    correlated_robustness=dict(rho_same=rs,rho_different=rd,direct_net=directc,total_net=totalc),
    scope='Exact arithmetic and analytic inequalities; not a literature novelty certificate or an unrestricted mechanism optimum.'))
OUT.write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
print(json.dumps({k:data[k] for k in ['status','threshold','direct_capacity_gain_net','total_policy_gain_net','correlated_robustness']},indent=2))
