import sys
input = sys.stdin.readline
n=int(input())
A,B,C,D = [],[],[],[]
nums=[]
for _ in range(n):
    a,b,c,d=map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
ab={}
cd={}
for a in A:
    for b in B:
        if a+b not in ab:
            ab[a+b]=1
        else:
            ab[a+b]+=1
for c in C:
    for d in D:
        if c+d not in cd:
            cd[c+d]=1
        else:
            cd[c+d]+=1

ans=0  
for x in ab:
    if -x in cd:
        ans+=(ab[x]*cd[-x])
        
print(ans)
