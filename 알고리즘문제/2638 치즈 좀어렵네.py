from collections import deque
from sys import stdin
input = stdin.readline
a,b=map(int,input().split())
board=[ list(map(int,input().split())) for _ in range(a)]

def bfs():
    q=deque()
    q.append([0,0])
    check=[[ False for _ in range(b)] for _ in range(a)]
    check[0][0]=True
    
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    while q:
        x,y = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx>=0 and nx<a and ny>=0 and ny<b:
                if not check[nx][ny]:
                    if board[nx][ny]>=1:
                        board[nx][ny]+=1
                    else:
                        q.append([nx,ny])
                        check[nx][ny]=True
   
cnt=0
while True:
    bfs()
    fin=False
   
    for x in range(a):
        for y in range(b):
            if board[x][y]>=3:
                board[x][y]=0
                fin=True
            elif board[x][y]==2:
                board[x][y]=1
    if fin:
        cnt+=1
    else:
        print(cnt)
        break
   
                        
        
