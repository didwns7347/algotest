import sys
from collections import deque
input= sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,-1,1]
def solve(q):
    hide=[ deque() for _ in range(26)]
    answer=0
    while q:
        x,y=q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<n+2 and 0<=ny<m+2:
                if board[nx][ny]=="." and check[nx][ny]==0:
                    q.append([nx,ny])
                    check[nx][ny]=1
                if 97<= ord(board[nx][ny]) <=122 and check[nx][ny]==0:
                    keyset.add(board[nx][ny])
                    get=ord(board[nx][ny])-97
                    while hide[get]:
                        a,b=hide[get].popleft()
                        q.append([a,b])
                    check[nx][ny]=1
                    q.append([nx,ny])
                        
                
                if 65<= ord(board[nx][ny]) <=90 and check[nx][ny]==0:
                    if chr(ord(board[nx][ny])+32) not in keyset:
                        hide[ord(board[nx][ny])-65].append([nx,ny])
                    else:
                        #print(nx,ny)
                        q.append([nx,ny])
                        check[nx][ny]=1
                    
                if board[nx][ny]=="$" and check[nx][ny]==0:
                    q.append([nx,ny])
                    check[nx][ny]=1
                    answer+=1
    return answer
            
for _ in range(int(input())):
    n,m=map(int,input().split())
    board=[]
    q=deque()
    check=[[0 for _ in range(m+2)] for _ in range(n+2)]
    cnt=0
    board.append(["."]*(m+2))
    for i in range(n):
        tmp=list("."+input().strip()+".")
        board.append(tmp)
    board.append(["."]*(m+2))
    keyset=set(input().strip())
    q.append([0,0])
    print(solve(q))
        
