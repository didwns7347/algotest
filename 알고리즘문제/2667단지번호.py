import sys
sys.setrecursionlimit(2000)
n=int(input())
m=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
part=[0 for x in range(626)]
out=[]
for x in range(n):
    t=sys.stdin.readline().strip()
    tmp=[]
    t=list(t)
    for s in t:
        tmp.append(int(s)) 
    m.append(tmp)
check=[[0 for x in range(n)] for _ in range(n)]
cnt=1
def dfs(x,y,cnt):
    check[x][y]=cnt
    part[cnt]+=1
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx and nx<n and 0<=ny and ny<n and check[nx][ny]==0 and m[nx][ny]==1:
            dfs(nx,ny,cnt)
    return 
for x in range(n):
    for y in range(n):
        if m[x][y]==1 and check[x][y]==0:
            dfs(x,y,cnt)
            cnt+=1

for x in part:
    if x!=0:
        out.append(x)
out.sort()
print(len(out))
for x in out:
    print(x)
