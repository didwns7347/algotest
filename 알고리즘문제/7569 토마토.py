from collections import deque
import sys
w,h,hh=map(int,input().split())
box=[]
for x in range(hh):
    b=[]
    for y in range(h):
        tmp=list(map(int,sys.stdin.readline().split()))
        b.append(tmp)
    box.append(b)

dist=[[[0 for x in range(w)] for y in range(h)] for z in range(hh)]
dx=[1,-1,0,0,0,0]
dy=[0,0,1,-1,0,0]
dz=[0,0,0,0,1,-1]
def BFS(x,y,z):
    check=[[[0 for x in range(w)] for y in range(h)] for z in range(hh)]
    dist[x][y][z]=1
    q=deque()
    q.append([x,y,z])
    check[x][y][z]=1
    while True:
        if not q:
            break
        tx,ty,tz=q.popleft()

        for i in range(6):
            nx,ny,nz=tx+dx[i],ty+dy[i],tz+dz[i]
            if nx>=0 and nx<hh and ny>=0 and ny<h and nz>=0 and nz<w:
                if check[nx][ny][nz]==0 and box[nx][ny][nz]==0:
                    if dist[nx][ny][nz]==0:
                        dist[nx][ny][nz]=dist[tx][ty][tz]+1
                                 
                    else:
                        dist[nx][ny][nz]=min(dist[tx][ty][tz]+1,dist[nx][ny][nz])
                    q.append([nx,ny,nz])
                    check[nx][ny][nz]=1
                if box[nx][ny][nz]==-1:
                    dist[nx][ny][nz]=-1
for x in range(hh):
    for y in range(h):
        for z in range(w):
            if box[x][y][z]==1:
                BFS(x,y,z)
def solve(hh,h,w):
    answer=-100
    for x in range(hh):
        for y in range(h):
            for z in range(w):
                if dist[x][y][z]==0:
                    return -1
                answer=max(answer,dist[x][y][z]-1)
    return answer
    
print(solve(hh,h,w))
                                
                
