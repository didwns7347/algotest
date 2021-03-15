board=[[0 for _ in range(10)] for _ in range(10)]
for i in range(10):
    tmp=list(input())
    for j in range(10):
        if tmp[j]=="O":
            board[i][j]=1
answer=0
def first(a,b):
    dx=[1,-1,0,0]
    dy=[0,0,-1,1]
    ck=True
    for i in range(4):
        na= a+dx[i]
        nb= b+dy[i]
        if na<0 or na>9 or nb<0 or nb>9:
            continue
        if board[na][nb]==0:
            ck=False
            break
    if ck:
        global answer
        answer+=1
        for i in range(4):
            na= a+dx[i]
            nb= b+dy[i]
            if na<0 or na>9 or nb<0 or nb>9:
                continue
            board[na][nb]=0
        board[a][b]=0

    
for i in range(10):
    for j in range(10):
        if board[i][j]==1:
            first(i,j)
for x in board:
    print(x)
               
