import critfun

def swap(i,j):
    k=i
    i=j
    j=k
    return i,j

def myperm(crit,m):
    from pandas.core.common import flatten
    k=len(m)
    n=sum(m)
    a=list(flatten([[i+1]*m[i] for i in range(k)]))
    h=[]
    dc={'Kruskal':critfun.Kruskal,'Wilcoxon':critfun.Wilcoxon,'Mood':critfun.Mood,'Ansari':critfun.Ansari,'Leman':critfun.Leman}
    h.append(dc[crit](a,k,n,m))
    kk = 0
    while True:
        j=n-2
        while j >=0 and a[j]>=a[j+1]:
            j=j-1
        if j<0:break
        kk=n-1
        while a[j]>=a[kk]:
            kk=kk-1
        a[j],a[kk]=swap(a[j],a[kk])
        lx=j+1
        r=n-1
        while lx<r:
            a[lx],a[r]=swap(a[lx],a[r])
            lx=lx+1
            r=r-1
        h.append(dc[crit](a,k,n,m))
    return h