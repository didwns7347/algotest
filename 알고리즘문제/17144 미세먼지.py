from sys import stdin
input=stdin.readline
import copy

n,m,t=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
tboard=[[0]*m for _ in range(n)]

r=[]

for x in range(n):
    if board[x][0]==-1:
        r.append(x)
tboard[r[0]][0]=-1
tboard[r[1]][0]=-1
def sprade(a,b):
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    cnt=0
    for i in range(4):
        na=a+dx[i]
        nb=b+dy[i]
        if na>=0 and na<n and nb>=0 and nb<m and board[na][nb]!=-1:
            cnt+=1
            tboard[na][nb]+=board[a][b]//5
    tboard[a][b]+=board[a][b]-cnt*(board[a][b]//5)
def rotate(u,d):
    tboard[u].insert(1,0)
    tmp=tboard[u].pop()
    tlist=[tmp]
    for x in range(u-1 ,-1,-1):
        tlist.append(tboard[x][m-1])
    tmp=tlist.pop()
   
    for x in range(0,u):
        tboard[x][m-1]=tlist.pop()
    
    tlist=[]
    for x in range(1,m-1):
        tlist.append(tboard[0][x])
    tlist.append(tmp)
    
    tmp=tboard[0][0]
    for x in range(0,m-1):
        tboard[0][x]=tlist[x]
    
    tlist=[tmp]
    for x in range(1,u):
        tlist.append(tboard[x][0])
    tlist.pop()
  
    for x in range(1,u):
        tboard[x][0]=tlist[x-1]


    tboard[d].insert(1,0)
    tmp=tboard[d].pop()
    tlist=[tmp]
    for x in range(d+1,n):
        tlist.append(tboard[x][m-1])
    tmp=tlist.pop()
    
    for x in range(d+1,n):
        
        tboard[x][m-1]=tlist[x-d-1]
  
    tlist=[]
    for x in range(1,m-1):
        tlist.append(tboard[n-1][x])
    tlist.append(tmp)
    tmp=tboard[n-1][0]
    for x in range(0,m-1):
        tboard[n-1][x]=tlist[x]
    tlist=[]
    for x in range(d+2,n-1):
        tlist.append(tboard[x][0])
    
    tlist.append(tmp)
 
    for x in range(d+1,n-1):
        tboard[x][0]=tlist[x-1-d]

    tlist=[]

        
    
cnt=0   
while True:
    for x in range(n):
        for y in range(m):
            if board[x][y]>0:
                sprade(x,y)
    
    rotate(r[0],r[1])
    cnt+=1
    if cnt==t:
        answer=0
        for x in tboard:
            answer+=sum(x)
        print(answer+2)
        break
    board=copy.deepcopy(tboard)
    tboard=[[0]*m for _ in range(n)]
    tboard[r[0]][0]=-1
    tboard[r[1]][0]=-1

