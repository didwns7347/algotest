import sys
from bisect import bisect_left
input = sys.stdin.readline
n=int(input())
line=[]

for _ in range(n):
    line.append(list(map(int,input().strip().split())))

line.sort()

link=dict()
num=[]
for a,b in line:
    link[b]=a
    num.append(b)

C=[num[0]]
res=[0]
ans=[0]
out=[]
for i in range(1,n):
    if C[-1]<num[i]:
        C.append(num[i])
        ans.append(len(C)-1)
    else:
        idx=bisect_left(C,num[i])
        C[idx]=num[i]
        ans.append(idx)
lgt=len(C)

for i in range(len(ans)-1,-1,-1):
    if ans[i]==lgt-1:
        out.append(num[i])
        lgt-=1

lst=set()

for x in range(len(out)-1,-1,-1):
    lst.add(out[x])
print(n-len(lst))
for x in num:
    if x not in lst:
        print(link[x])
        
