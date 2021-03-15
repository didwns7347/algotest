from itertools import combinations
import copy
from collections import deque
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
board=[list(map(int,input().split())) for x in range(n)]
house=[]
bbq=[]
c=0
ans=200*100

for x in range(n):
    for y in range(n):
        if board[x][y]==1:
            house.append([x,y])
        if board[x][y]==2:
            c+=1
            bbq.append([x,y])

cb=list(combinations(bbq,c-m))

def solve(t):
    m=copy.deepcopy(board)
    for x in t:
        m[x[0]][x[1]]=0
    return calc(m)
def calc(m):
    v=0
    for x in house:
        print(v)
        cnt=0
        q=deque()
        q.append([x[0],x[1]])
        while q:
            a,b=q.popleft()
            if m[a][b]==2:
                break
            cnt+=1
            for i in range(4):
                if a+dx[i]>=0 and a+dx[i]<n and b+dy[i]>=0 and b+dy[i]<n:
                    if m[a+dx[i]][b+dy[i]]!=1:
                        q.append([a+dx[i],b+dy[i]])
        v+=cnt
    return v
                        
if cb:    
    for x in cb:
        ans=min(ans,solve(x))
    else:
        ans=calc(board)
print(ans)
