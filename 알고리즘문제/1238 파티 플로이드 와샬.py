from sys import stdin
input=stdin.readline

N,M,X=map(int,input().split())
g=[[float("inf") for _ in range(N+1)] for _ in range(N+1)]
for _ in range(M):
    a,b,c=map(int,input().split())
    g[a][b]=c
for x in range(1,N+1):
    g[x][x]=0
for x in range(1,N+1):
    for y in range(1,N+1):
        if g[y][x]==float("inf") or y==X:
            continue
        for z in range(1,N+1):
            if g[x][z]==float("inf") or x==X:
                continue              
            if g[y][z]>g[y][x]+g[x][z]:
                g[y][z]=g[y][x]+g[x][z]
answer=0

for x in range(1,N+1):
    answer=max(answer,g[x][X]+g[X][x])
print(answer)
