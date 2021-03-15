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
    fin=True
    ne=200000000000
    for sd in range(1,7):
        if sd>=size:
            break
        if food[sd]>0:
            fin=False
    if fin:
        print(dist)
        break
    
    
    check=[[0 for _ in range(n)] for _ in range(n)]
    distl=[[dist for _ in range(n)] for _ in range(n)]
    q=deque()
    q.append([sx,sy])


    while q:
        x,y=q.popleft()
        check[x][y]=1
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n and 0<=ny<n and check[nx][ny]==0:
                if 0<= board[nx][ny]<=size:
                    distl[nx][ny]=distl[x][y]+1
                    q.append([nx,ny])


    ck=dist
    
    for a in range(len(check)):
        for b in range(len(check)):
            if check[a][b]!=0  and 0<board[a][b]<size :
                if ne>distl[a][b]:
                    ne=distl[a][b]
                    dist=distl[a][b]
                    sx,sy=a,b
                    name=board[a][b]

    '''for bd in board:
        print(bd)
    print()
    for ccc in check:
        print(ccc)
    print()
    for ddd in distl:
        print(ddd)
    print()'''
    if 0<name<size:
        food[name]-=1
        if cnt<size:
            cnt+=1
        if cnt==size:
            size+=1
            cnt=0
        board[sx][sy]=0
    
    


                
                        

