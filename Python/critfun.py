###################################################
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
            r1=r1+(i-k1)**2
            k1=k1+1
        if(a[i]==2):
            r2=r2+(i-k2)**2
            k2=k2+1
    zleman=(r1*m[0]+r2*m[1]+m[0]*m[1]/6)/(m[0]*m[1])**2-2/3
    return(zleman)
########################################################################
def Ansari(a,k,n,m):
    r=0
    for i in range(n):
        if (a[i]==1): r=r+((n+1)/2-abs(i+1-(n+1)/2))
    return(r)
