from collections import deque
answer=0
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def solution(board):
    cnt=0
    haed=[0,1]
    tail=[0,0]
    q=deque()
    q.append([haed,tail])
    board[0][1]=1
    while q:
        print(q)
        h,t=q.pop()
        cnt+=1
        if h[0]==len(board)-1 and h[1]==len(board)-1:
            break
        if t[0]==len(board)-1 and t[1]==len(board)-1:
            break
        
        for x in range(4):
            nh=[h[0]+dx[x],h[1]+dy[x]]
            nt=[t[0]+dx[x],t[1]+dy[x]]
            if check_range(h,t,dx[x],dy[x],board):
                if board[nh[0]][nh[1]]==0:
                    board[nh[0]][nh[1]]=cnt
                    q.append([nh,nt])
        if spin(h,t,board):
            nh,nt=spin(h,t,board)
            if board[nh[0]][nh[1]]==0:
                board[nh[0]][nh[1]]=cnt
                q.append([nh,nt])
    return board[-1][-1]
                
            
    
def spin(head,tail,board):
    if head[0]==tail[0] and tail[0]-1>=0 and tail[1]+1<len(board):
        if board[tail[0]-1][tail[1]+1]==1:
            return False
        head,tail=[tail[0]-1,tail[1]+1],head
        return [haed,tail]
    else:
        if tail[0]+1<len(board) and tail[1]+1<len(board):
            if board[tail[0]+1][tail[1]+1]==1:
                return False
            tail=[tail[0]+1,tail[1]+1]
            return [haed,tail]
def check_range(h,t,dx,dy,board):
    hi=len(board)
    w=len(board)
    hcheck=False
    tcheck=False
    if h[0]+dx>=0 and h[0]+dx<hi and h[1]+dy>=0 and h[1]+dy<w and board[h[0]+dx][h[1]+dy]==0:
        hcheck=True
    if t[0]+dx>=0 and t[0]+dx<hi and t[1]+dy>=0 and t[1]+dy<w and board[t[0]+dx][t[1]+dy]==0:
        tcheck=True
    if hcheck and tcheck:
        return True
    return False
print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
