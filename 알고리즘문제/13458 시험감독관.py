import math
n=int(input())

a=list(map(int,input().split()))

b,c=map(int,input().split())
ans=0
for x in a:
    if x-b<=0:
        ans+=1
    else:
        ans+=
        t=x-b
        ans+=math.ceil(float(t/c))        
        
print(ans)
