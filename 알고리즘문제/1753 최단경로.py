from collections import deque
from sys import stdin
input=stdin.readline
v,e=map(int,input().split())
start = int(input())
check=[False for _ in range(v+1)]
cost=[10*v for _ in range(v+1)]

out=[]
g=[[] for _ in range(v+1)]
for x in range(e):
    tu,tv,tw=map(int,input().split())
    g[tu].append([tv,tw])

q=deque()
q.append(start)
check[start]=True
cost[start]=0
while q:
    nex=q.popleft()
    for ne,val in g[nex]:
        if ne != start:
            cost[ne]=min(cost[ne],cost[nex]+val)
        if not check[ne] :  
            check[ne]=True
            q.append(ne)
        

for x in range(1,v+1):
    if not check[x]:
        print("INF")
        continue
    else:
        print(cost[x])
