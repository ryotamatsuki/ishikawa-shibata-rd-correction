import numpy as np
import matplotlib.pyplot as plt


def paper_xn(A,C,G,L,B1,B2):
    def d1(B): return 2*(2-B)+L*(1-3*B-2*L+(1+B)*L**2)
    def d2(B): return 2*((2-B+B*L)*(2-B-L)-L*(2*B-1+L)*(2*B-1-B*L))
    def d3(Bi,Bj): return ((2-Bi-L)*(2*Bj-1+L)+(2-Bi+Bi*L)*(2*Bj-1-Bj*L)-L*((2-Bj-L)*(2*Bi-1+L)+(2-Bj+Bj*L)*(2*Bi-1-Bi*L)))
    d4=G*(3-L)**2*(1+L); d11,d21=d1(B1),d1(B2); d12,d22=d2(B1),d2(B2); d13,d23=d3(B1,B2),d3(B2,B1)
    den=(d4-d12)*(d4-d22)-d13*d23
    return ((d11*(d4-d22)+d21*d13)*(A-C)/den,(d21*(d4-d12)+d11*d23)*(A-C)/den)


def paper_xc(A,C,G,L,B1,B2):
    def p1(B): return 2*(1+L)*(1-L)*(1+B)
    def p2(B): return 2*((2-B+B*L)*(2-B-L)+(2*B-1+L)*(2*B-1-B*L))
    def cross(Bi,Bj): return ((2-Bi-L)*(2*Bj-1+L)+(2-Bi+Bi*L)*(2*Bj-1-Bj*L))
    p3=cross(B1,B2)+cross(B2,B1); p4=G*(3-L)**2*(1+L)/(1-L); p11,p21=p1(B1),p1(B2); p12,p22=p2(B1),p2(B2)
    den=(p4-p12)*(p4-p22)-p3**2
    return ((p11*(p4-p22)+p21*p3)*(A-C)/den,(p21*(p4-p12)+p11*p3)*(A-C)/den)


def da(B1,B2,G):
    xn=paper_xn(100.0,50.0,G,0.0,B1,B2); xc=paper_xc(100.0,50.0,G,0.0,B1,B2)
    return sum(xn)-sum(xc)


def main():
    n=501; b=np.linspace(0,1,n); X,Y=np.meshgrid(b,b); styles=['-','--','-.']
    fig,ax=plt.subplots(figsize=(5.2,5.0))
    for G,ls in zip((10.0,50.0,100.0),styles):
        Z=np.empty_like(X)
        for i in range(n):
            for j in range(n):
                try: Z[i,j]=da(X[i,j],Y[i,j],G)
                except ZeroDivisionError: Z[i,j]=np.nan
        ax.contour(X,Y,Z,levels=[0],colors='black',linestyles=[ls],linewidths=1.3)
        ax.plot([],[],linestyle=ls,color='black',linewidth=1.3,label=rf'Corrected $D_A=0$, $\gamma={int(G)}$')
    ax.plot(b,1-b,':',color='black',linewidth=1.2,label=r'Published line $\beta_1+\beta_2=1$')
    ax.plot([0.5],[0.5],marker='o',markersize=4,color='black')
    ax.annotate(r'$(1/2,1/2)$',xy=(0.5,0.5),xytext=(0.56,0.43),fontsize=9,arrowprops=dict(arrowstyle='-',linewidth=0.7,color='black'))
    ax.set_xlim(0,1); ax.set_ylim(0,1); ax.set_xlabel(r'$\beta_1$'); ax.set_ylabel(r'$\beta_2$')
    ax.legend(frameon=False,fontsize=8,loc='lower left'); ax.set_aspect('equal',adjustable='box'); fig.tight_layout()
    fig.savefig('aggregate_boundary.pdf',bbox_inches='tight')


if __name__=='__main__': main()
