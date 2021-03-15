n=int(input())
A,B,C,D={},{},{},{}
num=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    if a not in A:
        A[a]=0
    else:
        A[a]+=1
    if b not in B:
        B[b]=0
    else:
        B[b]+=1
    if c not in C:
        C[c]=0
    else:
        C[c]+=1
    if d not in D:
        D[d]=0
    else:
        D[d]+=1
    num.append(a)
    num.append(b)
    num.append(c)
    num.append(d)

        
num.sort()
 
