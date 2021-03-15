import copy
h,w=map(int,input().split())
board=[]
test=[]
dy=[1,-1,0,0]
dx=[0,0,-1,1]
c=[
    [[0],[1],[2],[3]],
    [[0,1],[2,3]],
    [[2,0],[0,3],[3,1],[1,2]],
    [[1,2,0],[2,0,3],[0,3,1],[3,1,2]],
    [[0,1,2,3]]
]
for x in range(h):
    tmp=list(map(int,input().split()))
    board.append(tmp)
for x in range(h):
    for y in range(w):
        if board[x][y]!=0 and board[x][y]!=6:
            test.append([x,y])

def BF(n,board):
    print()
    for x in board:
        print(x)
    bd=copy.deepcopy(board)
    if n==len(test):
        cnt=0
        for x in board:
            for y in x:
                if y=='#':
                    cnt+=1
        return cnt
    a,b=test[n]
    see=c[board[a][b]]
    for x in see:
        BF(n+1,fill(bd,x,a,b))
        bd=copy.deepcopy(board)

def fill(b,d,x,y): 
    for dist in d:
        nx=x
        ny=y
        while True:
            nx=nx+dx[dist]
            ny=ny+dy[dist]
            if nx>=h or nx<0 or ny>=w or ny<0:
                break
            if b[nx][ny]==6:
                break
            if b[nx][ny]!=0:
                continue
            b[nx][ny]="#"
    return b
answer=0
print(BF(0,board))

        