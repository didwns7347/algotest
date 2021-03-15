'''from collections import deque
import copy
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def solution(board):
    n=len(board)
    a=[0,0]
    b=[0,1]
    hcheck=copy.deepcopy(board)
    tcheck=copy.deepcopy(board)
    q=deque()
    q.append([a,b])
    while q:
        t,h=q.popleft()
        for x in range(4):
            hx,hy=h[0]+dx[i],h[1]+dy[i]
            tx,ty=t[0]+dx[i],t[1]+dy[i]
            if hcheck[hx][hy]==0 or tcheck[tx][ty]==0 and board[hx][hy]==0 and board[tx][ty]==0:
                if hcheck[hx][hy]==0:
                    hcheck[hx][hy]=hcheck[h[0]][h[1]]+1
                if tcheck[tx][ty]==0:
                    tcheck[tx][ty]=tcheck[t[0]][t[1]]+1
                q.append([[tx,ty],[hx,hy]])
        hx,hy=tup(t,h)
        if hcheck[hx][hy]==0 and board[hx][hy]==0:
            hcheck[hx][hy]=hcheck[h[0]][h[1]]+1
            q.append([hx,hy],t)
        hx,hy=tdwon(t,h)
        if hcheck[hx][hy]==0 and board[hx][hy]==0:
            hcheck[hx][hy]=hcheck[h[0]][h[1]]+1
            q.append([hx,hy],t)
        tx,ty=hup(t,h)
        if tcheck[tx][ty]==0 and board[tx][ty]==0:
            tcheck[tx][ty]=tcheck[t[0]][t[1]]+1
            q.append(h,[tx,ty])
        tx,ty=hdwon(t,h)
        if tcheck[tx][ty]==0 and board[tx][ty]==0:
            tcheck[tx][ty]=tcheck[t[0]][t[1]]+1
            q.append(h,[tx,ty])
    answer = 0
    return answer'''
