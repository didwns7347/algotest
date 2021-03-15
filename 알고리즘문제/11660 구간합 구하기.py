from sys import stdin

input=stdin.readline
n,m=map(int,input().split())

board=[ list(map(int,input().split())) for _ in range(n)]
dist=[[0 for _ in range(n)] for _ in range(n)]


dist[0][0]=board[0][0]
for x in range(1,n):
    dist[x][0]+=dist[x-1][0]+board[x][0]
    dist[0][x]+=dist[0][x-1]+board[0][x]

for x in range(1,n):
    for y in range(1,n):
        dist[x][y]=dist[x-1][y]+dist[x][y-1]+board[x][y]-dist[x-1][y-1]


for _ in range(m):
    sx,sy,fx,fy=map(int,input().split())
    sx,sy,fx,fy=sx-1,sy-1,fx-1,fy-1
    if sx==0 and sy!=0:
        answer=dist[fx][fy]-dist[fx][sy-1]
    elif sy==0 and sx!=0:
        answer=dist[fx][fy]-dist[sx-1][fy]
    elif sx==0 and sy==0:
        answer=dist[fx][fy]
    else:
        answer=dist[fx][fy]-dist[sx-1][fy]-dist[fx][sy-1]+dist[sx-1][sy-1]        
    print(answer)
