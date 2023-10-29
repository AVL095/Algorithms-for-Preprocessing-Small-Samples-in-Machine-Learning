from scipy import stats
from more_itertools import distinct_permutations as dp
import pandas as pd
import numpy as np
from pandas.core.common import flatten
from time import time

############################################################################
def Mood(a,k,n,m):
    msmal=2
    if (m[0] < m[1]): msmal = 1
    r= 0
    for i in range(n):
        if (a[i]==msmal): r=r+(i+1-(n+1)/2)**2
    return(r)
###################################################
def Wilcoxon(a,k,n,m):
    msmal=2
    if (m[0] < m[1]): msmal = 1
    r= 0
    for i in range(n):
        if (a[i]==msmal): r=r+i+1
    return(r)
###################################################
def Kruskal(a,k,n,m):
    s=0
    for j in range(k):
        r=0
        for i in range(n):
            if(a[i]==j+1): r=r+i+1
        s=s+r*r/m[j]
    return(12.*s/(1.*n*(n+1.))-3.*(1.*n+1.))
####################################################
def Leman(a,k,n,m):
    r1 = 0; r2 = 0; k1 = 0; k2 = 0
    for i in range(n):
        if(a[i]==1):
            r1=r1+(i+1-k1)**2
            k1=k1+1
        if(a[i]==2):
            r2=r2+(i+1-k2)**2
            k2=k2+1
    zleman=(r1*m[0]+r2*m[1]+m[0]*m[1]/6)/(m[0]*m[1])**2-2/3
    return(zleman)
#######################################################################
def David(a,k,n,m):
    msmal=2
    if(m[0]<m[1]): msmal = 1
    r=0
    for i in range(n):
        if a[i]==msmal:
            if i<=n/2: r+=n/2-i
            if i>n/2: r+=i-n/2-1
    return(r)
########################################################################
def Ansari(a,k,n,m):
    r=0
    for i in range(n):
        if (a[i]==1): r=r+((n+1)/2-abs(i+1-(n+1)/2))
    return(r)
 ################################Чтение данных###################################################       
def rank_exact(crit,m):
    a=[]
    k=len(m)
    n=sum(m)
    dc={'Kruskal':Kruskal,'Wilcoxon':Wilcoxon,'Mood':Mood,'Ansari':Ansari,'Leman':Leman,'David':David}
    fname=dc[crit]
    a=list(flatten([[i+1]*m[i] for i in range(k)]))
    now = time()
    h=pd.Series(map(lambda xx:fname(xx,k,n,m),dp(a)))
    kx=len(h)
    xx=h.value_counts().sort_index()
    kk=len(xx)
    w=xx.index
    w=np.array(w)
    pw=xx.values/sum(xx.values)
    pw=np.array(pw)
    s1=0
    for i in range(kk):
         s1+=pw[i]; pw[i]=s1
    stime=time()-now
    return(kx,kk,stime,w,pw)

#########################################################################
def Exact(crit):
    if crit=="Ansari":
        x1=stats.norm.rvs(loc=0,scale=1,size=m[0])
        x2=stats.norm.rvs(loc=0,scale=1,size=m[1])
        AB,pval,astart,a1=stats.ansari(x1,x2)
        hnum=len(a1)
        kk=hnum
        total=a1.sum()
        pw=[astart+i for i in range(hnum)]
        w=[sum(a1[0:i+1]/total) for i in range(hnum)]
        stime=0
    else:  
        [hnum,kk,stime,pw,w]=rank_exact(crit,m)
    return(hnum,kk,stime,pw,w)

###########################################################

crit="Mood"
txt="Inp/"+crit+".inp"
finp=open(txt)
st=finp.readline()
m=tuple(map(int,finp.readline().split()))
finp.close()

(hnum,kk,stime,pw,w)=Exact(crit)

txt="Out/"+crit+".out"
fout=open(txt,'w')
print("Time: ",stime,file=fout) 
print("Criterion: ",crit,file=fout) 
print("Samples: ",m,file=fout)
print("Sum: ",sum(m),file=fout)
print("Variants: ",hnum,file=fout)
print("Size: ",kk,file=fout)
print("Statistics",pw,file=fout)
print("P-value",w,file=fout)
fout.close()
