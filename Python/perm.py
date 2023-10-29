import pandas as pd


def full(A):
    while True:
        yield tuple(A)
        for i in range(size-2,-1,-1):
            if A[i] < A[i + 1]:
                break
        else:
            return
        for j in range(size-1,i,-1):
            if A[i] < A[j]:break
        A[i], A[j] = A[j], A[i]
        A[i + 1 :] = A[: i - size : -1]
                
a=[1,1,1,2,2,2,2,3,3,3,3,4,4,4,4]
size=len(a)
s=pd.Series(full(a))
print(s)