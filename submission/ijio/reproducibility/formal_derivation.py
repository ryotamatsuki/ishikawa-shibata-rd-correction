"""Reviewer-safe exact verification for the Ishikawa-Shibata correction."""
from __future__ import annotations
import sympy as sp

A,C,G,L,B1,B2,b,s,d = sp.symbols("A C G L B1 B2 b s d")

def paper_xn(A,C,G,L,B1,B2):
    def d1(B): return 2*(2-B)+L*(1-3*B-2*L+(1+B)*L**2)
    def d2(B): return 2*((2-B+B*L)*(2-B-L)-L*(2*B-1+L)*(2*B-1-B*L))
    def d3(Bi,Bj): return ((2-Bi-L)*(2*Bj-1+L)+(2-Bi+Bi*L)*(2*Bj-1-Bj*L)-L*((2-Bj-L)*(2*Bi-1+L)+(2-Bj+Bj*L)*(2*Bi-1-Bi*L)))
    d4=G*(3-L)**2*(1+L); d11,d21=d1(B1),d1(B2); d12,d22=d2(B1),d2(B2); d13,d23=d3(B1,B2),d3(B2,B1)
    den=(d4-d12)*(d4-d22)-d13*d23
    return (sp.cancel((d11*(d4-d22)+d21*d13)*(A-C)/den),sp.cancel((d21*(d4-d12)+d11*d23)*(A-C)/den))

def paper_xc(A,C,G,L,B1,B2):
    def p1(B): return 2*(1+L)*(1-L)*(1+B)
    def p2(B): return 2*((2-B+B*L)*(2-B-L)+(2*B-1+L)*(2*B-1-B*L))
    def cross(Bi,Bj): return ((2-Bi-L)*(2*Bj-1+L)+(2-Bi+Bi*L)*(2*Bj-1-Bj*L))
    p3=cross(B1,B2)+cross(B2,B1); p4=G*(3-L)**2*(1+L)/(1-L); p11,p21=p1(B1),p1(B2); p12,p22=p2(B1),p2(B2)
    den=(p4-p12)*(p4-p22)-p3**2
    return (sp.cancel((p11*(p4-p22)+p21*p3)*(A-C)/den),sp.cancel((p21*(p4-p12)+p11*p3)*(A-C)/den))

xn=paper_xn(A,C,G,L,B1,B2); xc=paper_xc(A,C,G,L,B1,B2)
D1=sp.factor(sp.cancel(xn[0]-xc[0])); DA=sp.factor(sp.cancel(sum(xn)-sum(xc)))

D1sl=sp.factor(sp.cancel(D1.subs({L:0,B2:0}))); n1,den1=map(sp.factor,sp.fraction(D1sl)); Q1=sp.factor(n1/(2*G*(A-C)))
Q1e=-27*(2*B1-1)*G**2+18*(2*B1**3-7*B1**2+12*B1-5)*G-4*(10*B1**3-35*B1**2+45*B1-18)
assert sp.expand(Q1-Q1e)==0
p1={B1:sp.Rational(1,3),G:sp.Rational(44,27)}
assert Q1.subs(p1)==0
assert sp.diff(Q1,G).subs(p1)==-sp.Rational(4,3)
assert sp.diff(Q1,B1).subs(p1)==-sp.Rational(236,27)
assert -sp.diff(Q1,G).subs(p1)/sp.diff(Q1,B1).subs(p1)==-sp.Rational(9,59)
assert den1.subs(p1)==sp.Rational(808640,19683)

nsym=sp.factor(sp.fraction(sp.cancel(D1.subs({B1:b,B2:b})))[0]); F=b*(L**2-3*L+4)+L**2-L-2
assert sp.factor(nsym+G*(A-C)*(L-3)**2*F)==0
bstar=sp.factor((2+L-L**2)/(L**2-3*L+4)); assert sp.factor(F.subs(b,bstar))==0

DA0=sp.factor(sp.cancel(DA.subs(L,0))); nA0,_=map(sp.factor,sp.fraction(DA0)); QA=sp.factor(nA0/(4*G*(A-C)))
Qsd=sp.factor(QA.subs({B1:(s+d)/2,B2:(s-d)/2})); assert sp.factor(Qsd.subs(s,1)-d**2*(18*G+d**2-9)/2)==0

DAsl=sp.factor(sp.cancel(DA.subs({L:0,B2:0}))); nAs,_=map(sp.factor,sp.fraction(DAsl)); QAs=sp.factor(nAs/(4*G*(A-C)))
H=10*B1**3-35*B1**2+18; assert sp.factor(QAs.subs(G,2)-2*B1*H)==0
lo,hi=sp.Rational(4097,5000),sp.Rational(1639,2000); assert H.subs(B1,lo)>0 and H.subs(B1,hi)<0
QG=sp.diff(QAs,G).subs(G,2); QB=sp.diff(QAs,B1).subs(G,2)
QGred=sp.factor(sp.rem(sp.Poly(QG,B1),sp.Poly(H,B1)).as_expr()); QBred=sp.factor(sp.rem(sp.Poly(QB,B1),sp.Poly(H,B1)).as_expr())
assert sp.expand(QGred+sp.Rational(9,5)*(25*B1**2-35*B1+8))==0
assert sp.expand(QBred-2*(35*B1**2-54))==0

ce={A:100,C:50,G:10,L:0,B1:sp.Rational(49,50),B2:0}; xnce=tuple(sp.factor(z.subs(ce)) for z in xn); xcce=tuple(sp.factor(z.subs(ce)) for z in xc)
assert xnce==(sp.Rational(110500,100239),sp.Rational(83220,33413))
assert xcce==(sp.Rational(44500,19119),sp.Rational(8300,6373))
SN=sp.factor(sum(xnce)); SC=sp.factor(sum(xcce)); GAP=sp.factor(SN-SC)
assert SN==sp.Rational(360160,100239); assert SC==sp.Rational(69400,19119); assert GAP==-sp.Rational(23562520,638823147) and GAP<0
assert sp.Rational(49,100)<sp.Rational(1,2)

print("STAGE5_REPRODUCIBILITY_PASS")
print("P1 derivative:", -sp.Rational(9,59))
print("P1 symmetric crossing:", bstar)
print("P2 root bracket:", lo,hi)
print("P3 aggregates/gap:", SN,SC,GAP)
