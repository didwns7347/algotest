n=int(input())
board=[]
for _ in range(n):
    board.append(list(map(int,input().split())))

pip=[0,0,0,1]
answer=0
def check(x,y):
    if x>=n or y>=n:
        return False
    return True
def BF(p,state,i):
    global answer
    tx,ty,hx,hy=p
    if hx==n-1 and hy==n-1:
        answer+=1
        return
    if state==1:
        if check(hx,hy+1) and board[hx][hy+1]==0 :
            BF([tx,ty+1,hx,hy+1],1,i+1)
        if check(hx+1,hy+1) and board[hx+1][hy+1]==0 and board[hx][hy+1]==0  and board[hx+1][hy]==0 :
            BF([tx,ty+1,hx+1,hy+1],3,i+1)

    elif state==2:
        if check(hx+1,hy) and board[hx+1][hy]==0 :
            BF([tx+1,ty,hx+1,hy],2,i+1)
        if check(hx+1,hy+1) and board[hx+1][hy+1]==0 and board[hx+1][hy]==0  and board[hx][hy+1]==0 :
            BF([tx+1,ty,hx+1,hy+1],3,i+1)
            

    elif state==3:
        if check(hx,hy+1) and board[hx][hy+1]==0 :
            BF([tx+1,ty+1,hx,hy+1],1,i+1)
        if check(hx+1,hy) and board[hx+1][hy]==0 :
            BF([tx+1,ty+1,hx+1,hy],2,i+1)
        if check(hx+1,hy+1) and board[hx+1][hy+1]==0 and board[hx][hy+1]==0 and board[hx+1][hy]==0 :
             BF([tx+1,ty+1,hx+1,hy+1],3,i+1)
BF(pip,1,0)
print(answer)
