import sys
sys.setrecursionlimit(2000)
board=[]
for x in range(5):
    tmp=list(map(int,input().split()))
    board.append(tmp)



dx=[1,-1,0,0]
dy=[0,0,-1,1]
def check(num,x,y,i):

    if i==6:
        if num not in answer:
            answer[num]=1
        return
    for idx in range(4):
        nx=x+dx[idx]
        ny=y+dy[idx]
        if 0<=nx and ny<5 and 0<=ny and nx<5:
            num=num*10 + board[nx][ny]
            check(num,nx,ny,i+1)
            num=num//10


answer={}
for x in range(5):
    for y in range(5):
        check(board[x][y],x,y,1)

print(len(answer))