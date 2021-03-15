check_x=[0 for x in range(12)]
check_y=[0 for x in range(12)]
dx=[1,-1,1,-1]
dy=[1,-1,-1,1]
answer=0
def solution(n):
    global answer 
    board=[[0 for _ in range(n)] for _ in range(n)]
    do(0,board,n)
    return answer

def do(i,board,n):
    if i==n:
        global answer
        answer+=1
        return 
    for x in range(n):
        if check(i,x,board,n) and check_x[x]==0:
            board[i][x]=1
            check_x[x]=1
            do(i+1,board,n)
            board[i][x]=0
            check_x[x]=0
    
    return 0
def check(x,y,board,n):
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        while True:
            if nx==x and ny==y:
                continue
            if nx<0 or nx>=n or ny<0 or ny>=n:
                break
            if board[nx][ny]==1 :
                return False
            nx=nx+dx[i]
            ny=ny+dy[i]
    return True
b=[[0,0,0],
   [1,0,0],
   [0,0,0]]
print(check(1,1,b,3))
print(solution(12))

