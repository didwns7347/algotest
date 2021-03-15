n=int(input())
from collections import deque
board=[]
food=[0 for x in range(7)]
for x in range(n):
    tmp=list(map(int,input().split()))
    for y in range(len(tmp)):
        if tmp[y]>0 and tmp[y]<9:
            food[tmp[y]]+=1
        if tmp[y]==9:
            sx,sy=x,y
    board.append(tmp)
board[sx][sy]=0
dx=[1,-1,0,0]
dy=[0,0,-1,1]
dist=0
size=2
cnt=0
itor=0
while True:
    ne=n*n
    if food[0:size]==[0]*size:
        print(dist-1)
        break
    check=[[dist for _ in range(n)] for _ in range(n)]
    q=deque()
    q.append([sx,sy])
    check[sx][sy]=dist+1
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny]==dist:
                if 0<= board[nx][ny]<size:
                    check[nx][ny]=check[x][y]+1
                    q.append([nx,ny])
    for asdf in check:
        print(asdf)
    print(dist)
    for a in range(len(check)):
        for b in range(len(check)):
            if check[a][b]!=dist and board[a][b]!=0 :
                if ne>check[a][b]:
                    ne=check[a][b]
                    dist=ne-1
                    sx,sy=a,b
    food[board[sx][sy]]-=1
    if cnt<size:
        cnt+=1
    else:
        size+=1
        cnt=0
    board[sx][sy]=0
    
    
    


                
                        

