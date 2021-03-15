from sys import stdin
import heapq
input=stdin.readline

n=int(input())
board=[list(map(int , input().split())) for _ in range(n)]
q=[]
dx=[-1,0,1,0]
dy=[0,-1,0,1]
def init():
    for i in range(n):
        for j in range(n):
            if board[i][j]==9:
                heapq.heappush(q,[0,i,j])
                board[i][j]=0
                return

def BFS():
    size,eat,ans=2,0,0
    check=[[False]*n for _ in range(n)]
    while q:
        dist,x,y=heapq.heappop(q)
        if 0<board[x][y]<size:
            eat+=1
            board[x][y]=0
            if eat==size:
                size+=1
                eat=0
            ans+=dist
            dist=0
            while q:
                q.pop()
            check=[[False]*n for _ in range(n)]
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            ndist=dist+1
            if nx<0 or nx>=n or ny<0 or ny>=n:
                continue
            if 0<board[nx][ny]>size or check[nx][ny]==1:
                continue
            check[nx][ny]=1
            heapq.heappush(q,[ndist,nx,ny])
    print(ans)
init()
BFS()
                
