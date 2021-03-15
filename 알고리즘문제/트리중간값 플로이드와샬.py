edges=[[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9], [6, 10], [10, 11]]
n=11

dist=[ [float("inf") for _ in range(n+1)] for _ in range(n+1)]
for a,b in edges:
    dist[a][b]=1
    dist[b][a]=1
for x in range(1,n+1):
    dist[x][x]=0
    for y in range(1,n+1):
        for z in range(1,n+1):
            if x==y or x==z or y==z:
                continue
            
            dist[x][z]=min(dist[x][z],dist[x][y]+dist[y][z])
answer=0
for x in dist:
    print(x)
for x in range(1,n+1):
    for y in range(x+1,n+1):
        for z in range(y+1,n+1):
            print(x,y,z)
            answer=max(answer,dist[x][y]+dist[y][z]+dist[x][z])
print(answer)
print(answer//3)
            
