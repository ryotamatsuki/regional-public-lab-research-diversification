#!/usr/bin/env python3
"""Independent exact-rational, primitive-level test of restricted nonlinear P2.

This tests one genuinely nonlinear N=3 economy, not a universal theorem.
The analytic general-N response is separately certified in Prop2N.lean.
"""
import sympy as sp

N = 3
A, g = sp.Integer(10), sp.Rational(1, 10)
k0, kappa = sp.Integer(1), sp.Integer(1)
a0, x0, delta = sp.Rational(1, 4), sp.Rational(1, 10), sp.Rational(1, 2)
a = sp.symbols("a0:3")
x = sp.symbols("x0:3")
qvars = sp.symbols("q0:6")
Qold, Qnew = sum(qvars[::2]), sum(qvars[1::2])
quality = [item for i in range(N) for item in (A, A + delta + x[i])]
gross = sum(quality[j]*qvars[j] - qvars[j]**3 / 3 for j in range(2*N))
gross -= g * (Qold**2 + Qnew**2) / 2
inverse_price = [sp.diff(gross, qi) for qi in qvars]
production = [v for i in range(N) for v in (1-a[i], a[i])]
repl = dict(zip(qvars, production))
P = [sp.expand(p.subs(repl)) for p in inverse_price]
V = sp.expand(gross.subs(repl))
CS = sp.expand(V - sum(P[j]*production[j] for j in range(2*N)))
Pi = [sp.expand(P[2*i]*(1-a[i]) + P[2*i+1]*a[i]
                - k0*a[i] - kappa*a[i]**2/2) for i in range(N)]
W = sum(Pi) + CS - sum(xj**2 for xj in x)
G = Pi[0] + CS/N - x[0]**2
D = sp.Matrix([P[2*i+1]-P[2*i]-k0-kappa*a[i] for i in range(N)])
point = {**{ai:a0 for ai in a}, **{xi:x0 for xi in x}}
assert all(sp.simplify(di.subs(point)) == 0 for di in D)
J = -D.jacobian(a).subs(point)
response = J.inv() * sp.Matrix([1, 0, 0])
direct_gap = sp.diff(G, x[0]) - sp.diff(W, x[0])
indirect_gap = sum((sp.diff(G, a[i]) - sp.diff(W, a[i]))*response[i]
                   for i in range(N))
actual = sp.simplify((direct_gap+indirect_gap).subs(point))
Lphi = kappa + 2*(1-a0) + 2*a0
expected = sp.Rational(N-1, N) * (2*(1-a0)**2 - 2*a0**2) / Lphi
assert J == sp.Matrix([[sp.Rational(16,5), sp.Rational(1,5), sp.Rational(1,5)],
                       [sp.Rational(1,5), sp.Rational(16,5), sp.Rational(1,5)],
                       [sp.Rational(1,5), sp.Rational(1,5), sp.Rational(16,5)]])
assert actual == expected == sp.Rational(2,9)
print("PASS: nonlinear 3-region gross utility -> six inverse prices ->")
print("      competitive adoption Jacobian -> total G minus W research wedge = 2/9.")
print("Scope: exact example only; not a generic proof or all-assumptions Lean certificate.")
