import math
a,b=map(int,input().split())
answer=abs(a-b)




def BF(n,m,i):
    global answer
    if i>answer:
        return
    if n<0 or n>m*2:
        return
    
    if n==m:
        answer=min(answer,i)
        return
    print(n,m,i)
    BF(n-1,m,i+1)
    BF(n+1,m,i+1)
    BF(n*2,m,i)

BF(a,b,0)
print(answer)
