w,h=map(int,input().split())
box=[]
d=[[-1 for x in range(w)]for y in range(h)]

s=[[0,1],[0,-1],[1,0],[-1,0]]
q=[]
for x in range(h):
    tmp=list(map(int, input().split()))
    box.append(tmp)
for x in range(h):
    for y in range(w):
        if box[x][y]==1:

            tmp=[]
            tmp.append(x)
            tmp.append(y)
            q.append(tmp)
            d[x][y]=0

while True:
    if not q:
        break
    tmp=q.pop(0)
    x=tmp[0]
    y=tmp[1]
    for c in s:
        nx,ny=x+c[0],y+c[1]
        if 0<=nx and nx<h and 0<=ny and ny<w:
            if box[nx][ny]==0 and d[nx][ny]==-1:

                d[nx][ny]=d[x][y]+1
                tmp=[]
                tmp.append(nx)
                tmp.append(ny)
                q.append(tmp)
ans = 0   
for i in range(h):
    for j in range(w):
        if ans<d[i][j]:
            ans=d[i][j]
for i in range(h):
    for j in range(w):
        if box[i][j]==0 and d[i][j]==-1:
            ans=-1

print(ans)
