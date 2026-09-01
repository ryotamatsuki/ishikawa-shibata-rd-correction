"""Stage 2 formal symbolic derivation for Ishikawa–Shibata correction.

Uses SymPy exact arithmetic to verify the three frozen propositions:
P1 individual threshold gamma dependence and symmetric cancellation;
P2 aggregate threshold asymmetry/gamma dependence;
P3 exact rational counterexample and local regularity.

No network access or randomization.
"""
from __future__ import annotations
import sympy as sp

A,C,G,L,B1,B2,b,s,d = sp.symbols("A C G L B1 B2 b s d")
x1,x2 = sp.symbols("x1 x2")

def paper_xn(A,C,G,L,B1,B2):
    def d1(B):
        return 2*(2-B) + L*(1-3*B-2*L+(1+B)*L**2)
    def d2(B):
        return 2*((2-B+B*L)*(2-B-L)-L*(2*B-1+L)*(2*B-1-B*L))
    def d3(Bi,Bj):
        return ((2-Bi-L)*(2*Bj-1+L)
                +(2-Bi+Bi*L)*(2*Bj-1-Bj*L)
                -L*((2-Bj-L)*(2*Bi-1+L)
                    +(2-Bj+Bj*L)*(2*Bi-1-Bi*L)))
    d4 = G*(3-L)**2*(1+L)
    d11,d21=d1(B1),d1(B2)
    d12,d22=d2(B1),d2(B2)
    d13,d23=d3(B1,B2),d3(B2,B1)
    den=(d4-d12)*(d4-d22)-d13*d23
    return (
        sp.cancel((d11*(d4-d22)+d21*d13)*(A-C)/den),
        sp.cancel((d21*(d4-d12)+d11*d23)*(A-C)/den),
    )

def paper_xc(A,C,G,L,B1,B2):
    def p1(B):
        return 2*(1+L)*(1-L)*(1+B)
    def p2(B):
        return 2*((2-B+B*L)*(2-B-L)+(2*B-1+L)*(2*B-1-B*L))
    def cross(Bi,Bj):
        return ((2-Bi-L)*(2*Bj-1+L)+(2-Bi+Bi*L)*(2*Bj-1-Bj*L))
    p3=cross(B1,B2)+cross(B2,B1)
    p4=G*(3-L)**2*(1+L)/(1-L)
    p11,p21=p1(B1),p1(B2)
    p12,p22=p2(B1),p2(B2)
    den=(p4-p12)*(p4-p22)-p3**2
    return (
        sp.cancel((p11*(p4-p22)+p21*p3)*(A-C)/den),
        sp.cancel((p21*(p4-p12)+p11*p3)*(A-C)/den),
    )

xn = paper_xn(A,C,G,L,B1,B2)
xc = paper_xc(A,C,G,L,B1,B2)
D1 = sp.factor(sp.cancel(xn[0]-xc[0]))
DA = sp.factor(sp.cancel(sum(xn)-sum(xc)))

# P1: asymmetric exact local gamma dependence, lambda=0,beta2=0.
D1_sl = sp.factor(sp.cancel(D1.subs({L:0,B2:0})))
n1,d1den = map(sp.factor, sp.fraction(D1_sl))
Q1 = sp.factor(n1/(2*G*(A-C)))
Q1_expected = (
    -27*(2*B1-1)*G**2
    +18*(2*B1**3-7*B1**2+12*B1-5)*G
    -4*(10*B1**3-35*B1**2+45*B1-18)
)
assert sp.expand(Q1-Q1_expected) == 0
p1 = {B1:sp.Rational(1,3), G:sp.Rational(44,27)}
assert sp.factor(Q1.subs(p1)) == 0
Q1G = sp.diff(Q1,G)
Q1B = sp.diff(Q1,B1)
assert sp.factor(Q1G.subs(p1)) == -sp.Rational(4,3)
assert sp.factor(Q1B.subs(p1)) == -sp.Rational(236,27)
assert sp.factor(-Q1G.subs(p1)/Q1B.subs(p1)) == -sp.Rational(9,59)
assert sp.factor(d1den.subs(p1)) == sp.Rational(808640,19683)

# P1 symmetric cancellation.
D1_sym = sp.factor(sp.cancel(D1.subs({B1:b,B2:b})))
n_sym,d_sym = map(sp.factor, sp.fraction(D1_sym))
F_sym = b*(L**2-3*L+4) + L**2-L-2
assert sp.factor(n_sym + G*(A-C)*(L-3)**2*F_sym) == 0
b_star = sp.factor((2+L-L**2)/(L**2-3*L+4))
assert sp.factor(F_sym.subs(b,b_star)) == 0

# P2: aggregate lambda=0 factorization and published line.
DA0 = sp.factor(sp.cancel(DA.subs(L,0)))
nA0,dA0 = map(sp.factor, sp.fraction(DA0))
QA = sp.factor(nA0/(4*G*(A-C)))
QA_sd = sp.factor(QA.subs({B1:(s+d)/2,B2:(s-d)/2}))
assert sp.factor(QA_sd.subs(s,1) - d**2*(18*G+d**2-9)/2) == 0
DA_line = sp.factor(sp.cancel(DA0.subs({B1:(1+d)/2,B2:(1-d)/2})))
DA_line_expected = (
    32*G*d**2*(A-C)
    / ((-6*G+d**2+3)*(36*G**2-20*G*d**2-36*G+d**4+6*d**2+9))
)
assert sp.factor(DA_line-DA_line_expected) == 0

# P2: local gamma dependence on lambda=0,beta2=0 at G=2.
DA_sl = sp.factor(sp.cancel(DA.subs({L:0,B2:0})))
nAs,dAs = map(sp.factor, sp.fraction(DA_sl))
QAs = sp.factor(nAs/(4*G*(A-C)))
QAs_G = sp.factor(sp.diff(QAs,G))
QAs_B = sp.factor(sp.diff(QAs,B1))
H = 10*B1**3-35*B1**2+18
assert sp.factor(QAs.subs(G,2) - 2*B1*H) == 0
lo,hi = sp.Rational(4097,5000), sp.Rational(1639,2000)
assert H.subs(B1,lo) > 0 and H.subs(B1,hi) < 0
assert sp.factor(sp.diff(H,B1)) == 10*B1*(3*B1-7)
QG_red = sp.factor(sp.rem(sp.Poly(QAs_G.subs(G,2),B1),sp.Poly(H,B1)).as_expr())
QB_red = sp.factor(sp.rem(sp.Poly(QAs_B.subs(G,2),B1),sp.Poly(H,B1)).as_expr())
assert sp.expand(QG_red + sp.Rational(9,5)*(25*B1**2-35*B1+8)) == 0
assert sp.expand(QB_red - 2*(35*B1**2-54)) == 0
den_g2 = sp.factor(dAs.subs(G,2))
assert den_g2 == 16*B1*(5*B1-8)*(3*B1**2-10*B1-7)
R = 25*B1**2-35*B1+8
assert 50*lo-35 > 0 and R.subs(B1,hi) < 0
assert 35*hi**2-54 < 0

# P3 exact rational counterexample.
ce={A:sp.Integer(100),C:sp.Integer(50),G:sp.Integer(10),L:0,
    B1:sp.Rational(49,50),B2:0}
xn_ce=tuple(sp.factor(z.subs(ce)) for z in xn)
xc_ce=tuple(sp.factor(z.subs(ce)) for z in xc)
assert xn_ce == (sp.Rational(110500,100239),sp.Rational(83220,33413))
assert xc_ce == (sp.Rational(44500,19119),sp.Rational(8300,6373))
SN=sp.factor(sum(xn_ce)); SC=sp.factor(sum(xc_ce)); GAP=sp.factor(SN-SC)
assert SN == sp.Rational(360160,100239)
assert SC == sp.Rational(69400,19119)
assert GAP == -sp.Rational(23562520,638823147)
assert GAP < 0
assert sp.Rational(49,100) < sp.Rational(1,2)
den_xn = [sp.factor(sp.denom(z).subs(ce)) for z in xn]
den_xc = [sp.factor(sp.denom(z).subs(ce)) for z in xc]
assert all(z != 0 for z in den_xn+den_xc)

# Primitive output and curvature checks.
def output_eq(A,C,L,B1,B2):
    den=(3-L)*(1+L)
    common=(1+L)*(A-C)/den
    q1=common+(2-B1+B1*L)/den*x1+(2*B2-1+L)/den*x2
    q2=common+(2*B1-1+L)/den*x1+(2-B2+B2*L)/den*x2
    return sp.factor(q1),sp.factor(q2)

q1,q2=output_eq(A,C,L,B1,B2)
price=A-q1-q2
mc1=C-x1-B2*x2
mc2=C-x2-B1*x1
pi1=sp.expand((price-mc1)*q1); pi2=sp.expand((price-mc2)*q2)
f1=sp.expand(pi1-L*pi2-G*x1**2/2); f2=sp.expand(pi2-L*pi1-G*x2**2/2)
h11=sp.factor(sp.diff(f1,x1,2)); h12=sp.factor(sp.diff(f1,x1,x2))
h22=sp.factor(sp.diff(f2,x2,2)); h21=sp.factor(sp.diff(f2,x2,x1))
Jdet=sp.factor(h11*h22-h12*h21)
joint=sp.expand(f1+f2)
jh11=sp.factor(sp.diff(joint,x1,2)); jh12=sp.factor(sp.diff(joint,x1,x2))
jh22=sp.factor(sp.diff(joint,x2,2)); Hdet=sp.factor(jh11*jh22-jh12**2)

p1full={A:100,C:50,G:sp.Rational(44,27),L:0,B1:sp.Rational(1,3),B2:0}
xnp=tuple(sp.factor(z.subs(p1full)) for z in xn)
xcp=tuple(sp.factor(z.subs(p1full)) for z in xc)
assert xnp == (sp.Rational(150,19),sp.Rational(540,19))
assert xcp == (sp.Rational(150,19),sp.Rational(1800,133))
for pair in (xnp,xcp):
    qv=(sp.factor(q1.subs(p1full).subs({x1:pair[0],x2:pair[1]})),
        sp.factor(q2.subs(p1full).subs({x1:pair[0],x2:pair[1]})))
    mcv=(sp.factor(mc1.subs(p1full).subs({x1:pair[0],x2:pair[1]})),
         sp.factor(mc2.subs(p1full).subs({x1:pair[0],x2:pair[1]})))
    assert all(v>0 for v in pair+qv+mcv)
curv1=tuple(sp.factor(z.subs(p1full)) for z in (h11,h22,Jdet,jh11,jh22,Hdet))
assert curv1 == (-sp.Rational(82,81),-sp.Rational(20,27),sp.Rational(1520,2187),
                 -sp.Rational(80,81),-sp.Rational(14,27),sp.Rational(532,2187))

for pair in (xn_ce,xc_ce):
    qv=(sp.factor(q1.subs(ce).subs({x1:pair[0],x2:pair[1]})),
        sp.factor(q2.subs(ce).subs({x1:pair[0],x2:pair[1]})))
    mcv=(sp.factor(mc1.subs(ce).subs({x1:pair[0],x2:pair[1]})),
         sp.factor(mc2.subs(ce).subs({x1:pair[0],x2:pair[1]})))
    assert all(v>0 for v in pair+qv+mcv)
curv_ce=tuple(sp.factor(z.subs(ce)) for z in (h11,h22,Jdet,jh11,jh22,Hdet))
assert curv_ce == (-sp.Rational(12211,1250),-sp.Rational(82,9),sp.Rational(33413,375),
                   -sp.Rational(2391,250),-sp.Rational(80,9),sp.Rational(6373,75))

xn_g2=tuple(sp.factor(sp.cancel(z.subs({A:100,C:50,G:2,L:0,B2:0}))) for z in xn)
xc_g2=tuple(sp.factor(sp.cancel(z.subs({A:100,C:50,G:2,L:0,B2:0}))) for z in xc)
assert sp.factor(xn_g2[0] - 50*(B1-2)/(3*B1**2-10*B1-7)) == 0
assert sp.factor(xn_g2[1] - 100*(B1**2-3*B1-1)/(3*B1**2-10*B1-7)) == 0
assert sp.factor(xc_g2[0] + 50/(5*B1-8)) == 0
assert sp.factor(xc_g2[1] + 50/(5*B1-8)) == 0

print("STAGE2_FORMAL_DERIVATION_PASS")
print("P1 d beta*/d gamma =", -sp.Rational(9,59))
print("P1 b*(lambda) =", b_star)
print("P2 G=2 root bracket =", (lo,hi))
print("P3 exact aggregates =", SN, SC, GAP)
print("P3 decimals =", sp.N(SN,15), sp.N(SC,15), sp.N(GAP,15))
