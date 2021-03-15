from collections import deque
import sys
n,m = map(int,input().split())
check=[[0 for _ in range(m)] for _ in range(n)]
dcheck=[[0 for _ in range(m)] for _ in range(n)]
ccheck=[[0 for _ in range(m)] for _ in range(n)]

dx=[1,-1,0,0]
dy=[0,0,1,-1]
board=[]
for x in range(n):
    tmp=list(input())
    b=[]
    for y in tmp:
        b.append(int(y))
    board.append(b)

check[0][0]=1
check[0][0]=1

q=deque()
q.append([0,0,0])
while q:
    tx,ty,boom=q.popleft()
    for i in  range(4):
        nx,ny=dx[i]+tx,dy[i]+ty
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==0 and check[nx][ny]==0 and boom==0:
                check[nx][ny]=check[tx][ty]+1
                q.append([nx,ny,boom])
            if board[nx][ny]==1 and dcheck[nx][ny]==0 and boom==0:
                dcheck[nx][ny]=check[tx][ty]+1
                q.append([nx,ny,1])
            if board[nx][ny]==0 and check[nx][ny]==0 and boom==1:
                if dcheck[nx][ny]==0:
                    dcheck[nx][ny]=dcheck[tx][ty]+1
                    q.append([nx,ny,1])
                    
                

            
                
        
            
if dcheck[n-1][m-1]==0 and check[n-1][m-1]==0:
    print(-1)   
elif dcheck[n-1][m-1]!=0 and check[n-1][m-1]==0:
    print(dcheck[n-1][m-1])
elif check[n-1][m-1]!=0 and dcheck[n-1][m-1]==0:
    print(check[n-1][m-1])
else:
    print(min(check[-1][-1],dcheck[-1][-1]))


