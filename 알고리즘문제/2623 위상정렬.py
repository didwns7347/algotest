from collections import deque
import sys
input = sys.stdin.readline
q=deque()
a,b=map(int,input().split())
indeg=[0 for _ in range(a+1)]
board=[[] for _ in range(a+1)]
for _ in range(b):
    tmp=list(map(int,input().split()))
    if tmp[0]==0:
        continue
    tmp=tmp[1:]
    for x in range(len(tmp)-1):
        board[tmp[x]].append(tmp[x+1])
        indeg[tmp[x+1]]+=1
'''print(indeg)
print()
for x in board:
    print(x)'''
for x in range(1,a+1):
    if indeg[x]==0:
        q.append(x)
out=[]
cnt=0
while True:
    if not q:
        break
    now=q.popleft()
    cnt+=1
    out.append(now)
    for nxt in board[now]:
        indeg[nxt]-=1
        if indeg[nxt]==0:
            q.append(nxt)
   
if cnt<a:
    print(0)
else:
    for x in out:
        print(x)
