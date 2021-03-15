

n=10000000
import sys
sys.setrecursionlimit(2000)
def solution(board):
    
    answer=500000000
    print(do(0,0,-1,0,board))
    
    return answer
def do(x,y,l,money,board):
    print(x,y)
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    global n
    if x==len(board)-1 and y==len(board)-1:
        n=min(money,n)
        return 
    for i in range(4):
        if i==inv(l) :
            continue
        if 0<=x+dx[i] and x+dx[i]<len(board) and 0<=y+dy[i] and y+dy[i]<len(board):
            if board[x+dx[i]][y+dy[i]]==0:
                if i==l or l==-1:
                    do(x+dx[i],y+dy[i],i,money+100,board)
                else:
                    do(x+dx[i],y+dy[i],i,money+500,board)
    return

def inv(x):
    if x==0:
        return 1
    if x==1:
        return 0
    if x==3:
        return 2
    if x==2:
        return 3
    if x==-1:
        return 5
b=[[0,0,0],[0,0,0],[0,0,0]]
solution([[0,0,0],[0,0,0],[0,0,0]])
