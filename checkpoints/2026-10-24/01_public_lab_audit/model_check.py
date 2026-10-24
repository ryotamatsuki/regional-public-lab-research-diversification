import sympy as s
import json
from pathlib import Path
R=s.Rational
def market(ra=None, rb=None, thetaA=R(1,25),thetaB=R(1,40),mu=R(1,10),c=R(21,500),d=R(1,2),ee=R(3,4)):
    kinds=['old','old']; owners=[0,1]; vals=[s.S.One,s.S.One]
    for i,r in enumerate([ra,rb]):
        if r:
            kinds.append(r);owners.append(i);vals.append(1+(thetaA if r=='A' else thetaB))
    n=len(kinds); M=s.eye(n)
    for j in range(n):
        for k in range(j):
            M[j,k]=M[k,j]=ee if kinds[j]==kinds[k] and kinds[j]!='old' else d
    Q=s.Matrix(n,n,lambda j,k:2*M[j,k] if owners[j]==owners[k] else M[j,k])
    v=s.Matrix(vals);q=Q.inv()*v;prices=v-M*q
    cs=(q.T*M*q)[0]/2
    profits=[sum(q[j]*prices[j] for j in range(n) if owners[j]==i) for i in range(2)]
    G=[profits[i]+mu*cs-c*int([ra,rb][i] is not None) for i in range(2)]
    W=sum(profits)+cs-c*(n-2)
    return dict(G=G,W=W,q=list(q),prices=list(prices))
def stats(**kw):
    base=market(**kw); states={}; a={};b={};V={};RR={};H={}
    for r in ['A','B']:
        st=market(r,None,**kw);a[r]=s.factor(st['G'][0]-base['G'][0]);b[r]=s.factor(st['G'][1]-base['G'][1]);V[r]=s.factor(st['W']-base['W'])
    for r in ['A','B']:
        for t in ['A','B']:
            st=market(r,t,**kw); RR[r+t]=s.factor(a[r]+b[t]-(st['G'][0]-base['G'][0]));H[r+t]=s.factor(V[r]+V[t]-(st['W']-base['W']))
    return a,b,V,RR,H
def dump(x):
    if isinstance(x,dict):return {k:dump(v) for k,v in x.items()}
    if isinstance(x,(list,tuple)):return [dump(v) for v in x]
    return {'exact':str(x),'decimal':float(x)}
if __name__=='__main__':
    a,b,V,RR,H=stats(); da=a['A']-a['B']; p=s.symbols('p',positive=True)
    rs=R(1,5); rd=R(1,100);hS=p*p+rs*p*(1-p);hD=p*p+rd*p*(1-p)
    # General current-innovation-rent limited enforcement upper bound for B-obedience
    maxB=s.factor(-p*da+hS*a['A']-hD*RR['BA'])
    maxA=s.factor(p*da-hD*RR['AB']+hS*a['B'])
    critical=s.solve(maxB/p,p)
    print(json.dumps(dump(dict(alpha=a,beta=b,V=V,R=RR,H=H,delta_alpha=da,critical=critical)),indent=2))
    print('maxB',maxB,'maxA',maxA)
    for pp in [R(1,1000),R(1,100),R(1,25),R(1,20),R(1,10),R(1,2)]:
        print('p',pp,'B',float(maxB.subs(p,pp)), 'A',float(maxA.subs(p,pp)))
