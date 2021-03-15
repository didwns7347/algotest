from sys import stdin
import heapq

input=stdin.readline
MAX=100000*100
n=int(input())
dist=[[100000*100 for  _ in range(n+1)] for _ in range(n+1)]
m=int(input())
for _ in range(m):
    a,b,c,=map(int,input().split())
    dist[a][a]=0
    dist[b][b]=0
    dist[a][b]=min(dist[a][b],c)

for x in range(1,n+1):
    for y in range(1,n+1):
        for z in range(1,n+1):
            if dist[y][x]+dist[x][z]<dist[y][z]:
                dist[y][z]=dist[y][x]+dist[x][z]
for x in range(1,n+1):
    for y in range(1,n+1):
        if dist[x][y]==MAX:
            print(0,end=" ")
            continue
        print(dist[x][y],end=" ")
    print()
