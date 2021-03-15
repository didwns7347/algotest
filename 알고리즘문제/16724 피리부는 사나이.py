import sys
from collections import deque

input=sys.stdin.readline
n,m = map(int,input().split())
board=[]
aset=set()
def BFS(q,area):
    global ans
    ck=-1
    tmp=[]
    while q:
        a,b=q.popleft()
        tmp.append([a,b])
        check[a][b]=area
        if board[a][b]=="D":
            if check[a+1][b]==0:
                q.append([a+1,b])
            else:
                ck=check[a+1][b]
        elif board[a][b]=="L":
            if check[a][b-1]==0:
                q.append([a,b-1])
            else:
                ck=check[a][b-1]
                    
        elif board[a][b]=="R":
            if check[a][b+1]==0:
                q.append([a,b+1])
            else:
                ck=check[a][b+1]
        else:
            if check[a-1][b]==0:
                q.append([a-1,b])
            else:
                ck=check[a-1][b]
    if ck != area:
        return
        
        
    else:
        ans+=1
    
        
            
ans=0     
    
for _ in range(n):
    board.append(list(input().strip()))
check=[[0 for _ in range(m)] for _ in range(n)]

area=1
for x in range(n):
    for y in range(m):
        if check[x][y]==0:
            q=deque()
            q.append([x,y])
            BFS(q,area)
            area+=1
            
print(ans)
