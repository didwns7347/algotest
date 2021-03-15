from collections import deque
def rever(st):
    if st=="D":
        return "U"
    if st=="U":
        return "D"
    if st=="R":
        return "L"
    else:
        return "R"

    
def solution(board):
    answer = 0
    ck=True
    size = len(board)
    go=[[1,0,"D"],[-1,0,"U"],[0,1,"R"],[0,-1,"L"]]
    gdict={"D":0,"U":1,"R":2,"L":3}

    q=deque()
    dist=[[[(float("inf")) for _ in range(4)] for _ in range(size)] for _ in range(size)]
    if board[0][1]==0:
        q.append([0,1,"R"])
        dist[0][1][2]=100
    if board[1][0]==0:
        q.append([1,0,"D"])
        dist[1][0][0]=100
    for x in range(4):
        dist[0][0][x]=0
    while q:
        x,y,look= q.popleft()
        for i in range(4):
            nx=x+go[i][0]
            ny=y+go[i][1]
            nlook=go[i][2]
            #print(x,y,nx,ny,nlook)
            if rever(look)==nlook:
                continue
            
            if 0<=nx<size and 0<=ny<size and board[nx][ny]==0:
                if nlook==look :
                    if dist[nx][ny][gdict[nlook]]>dist[x][y][gdict[look]]+100:
                        dist[nx][ny][gdict[nlook]]=dist[x][y][gdict[look]]+100
                        q.append([nx,ny,nlook])
                else:
                    if dist[nx][ny][gdict[nlook]]>dist[x][y][gdict[look]]+600:
                        dist[nx][ny][gdict[nlook]]=dist[x][y][gdict[look]]+600
                        q.append([nx,ny,nlook])
    for x in dist:
        print(x)
    answer=min(dist[size-1][size-1])
    return answer
bd=[[0,0,0],[0,0,0],[0,0,0]]
print(solution(bd))
bd= [[0, 0, 0, 0, 0, 0, 0, 1],
     [0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 1],
     [0, 0, 1, 0, 0, 0, 1, 0],
     [0, 1, 0, 0, 0, 1, 0, 0],
     [1, 0, 0, 0, 0, 0, 0, 0]]
print(solution(bd))

    
