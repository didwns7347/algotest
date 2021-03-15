from collections import deque
import math
def solution(board):
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    ed=len(board)
    answer = 0
    q=deque()
    dist=[[math.inf for x in range(len(board))] for y in range(len(board))]
    check=[[ [0 for i in range(4)] for x in range(ed)] for y in range(ed)]
   
    q.append([0,0,-1])
    check[0][0]=1
    dist[0][0]=0
    while q:
        a,b,l=q.popleft()
        for i in range(4):
            na=a+dx[i]
            nb=b+dy[i]
            
            if a+dx[i]>=0 and a+dx[i]<ed and b+dy[i]>=0 and b+dy[i]<ed:
                if board[na][nb] == 0 and check[na][nb][i]==0:
                    check[na][nb][i]=1
                    if l==-1 or i==l:
                        dist[na][nb]=min(dist[na][nb],dist[a][b]+100)
                        q.append([na,nb,i])
                    else:
                        dist[na][nb]=min(dist[na][nb],dist[a][b]+600)
                        q.append([na,nb,i])
    for x in dist:
        print(x)
                    
    answer=dist[ed-1][ed-1]
    return answer
m=[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
for x in m:
    print(x)
print(solution(m))
