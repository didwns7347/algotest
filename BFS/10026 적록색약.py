import sys
sys.setrecursionlimit(2000)
n=int(input())
answer=0
board=[]
boardRG=[]
dx=[1,-1,0,0]
dy=[0,0,1,-1]
check=[[False for _ in range(n)] for _ in range(n)]
checkRG=[[False for _ in range(n)] for _ in range(n)]
for x in range(n):
    board.append(list(input()))
for x in range(n):
    tmp=[]
    for y in range(n):
        if board[x][y]=="G":
            tmp.append("R")
        else:
            tmp.append(board[x][y])
    boardRG.append(tmp)
def DFS(a,b):
    check[a][b]=True
    for x in range(4):
        nx=a+dx[x]
        ny=b+dy[x]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if check[nx][ny]==False and board[nx][ny]==board[a][b]:
                DFS(nx,ny)
def DFSRG(a,b):
    checkRG[a][b]=True
    for x in range(4):
        nx=a+dx[x]
        ny=b+dy[x]
        if 0<=nx and nx<n and 0<=ny and ny<n:
            if checkRG[nx][ny]==False and boardRG[nx][ny]==boardRG[a][b]:
                DFSRG(nx,ny)

for x in range(n):
    for y in range(n):
        if check[x][y]==False:
            DFS(x,y)
            answer+=1
RGanswer=0
for x in range(n):
    for y in range(n):
        if checkRG[x][y]==False:
            DFSRG(x,y)
            RGanswer+=1
print(answer,RGanswer)