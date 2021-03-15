N,M = map(int,input().split())

board=[ list(map(int,input().split())) for _ in range(N)]
tmp=[]
for x in board:
    for y in x:
        if y==1:
            tmp.append(1)
def check(x,y):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    cnt=0
    for i in range(4):
        nx=x+dx[i]
        ny=y+dy[i]
        if 0<=nx<N and 0<=ny<M:
            if board[nx][ny]==0:
                cnt+=1
    return cnt
answer=0
while True:
    tmp=[]
    answer+=1
    
    
    for x in range(N):
        for y in range(M):
            if board[x][y]==1:
                if check(x,y)>1:
                    tmp.append([x,y])
    if not tmp:
        break
    for fuck in tmp:
        board[fuck[0]][fuck[1]]=0
                
   
                
    
print(answer-1)
