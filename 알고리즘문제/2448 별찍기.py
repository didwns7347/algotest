n=int(input())
board=[[" " for _ in range(n*2)] for _ in range(n)]
def star(x,y,a,b):
    xt=(a-x)
    yt=(b-y)//4
    if xt==3:
        board[x][y+2]="*"
        board[x+1][y+1]="*"
        board[x+1][y+3]="*"
        board[x+2][y]="*"
        board[x+2][y+1]="*"
        board[x+2][y+2]="*"
        board[x+2][y+3]="*"
        board[x+2][y+4]="*"
        return
    star(x,y+yt,x+xt//2,y+3*yt)
    star(x+xt//2,y,x+xt,y+yt*2)
    star(x+xt//2,y+2*yt,x+xt,y+4*yt)

star(0,0,n,n*2)
for x in board:
    for y in x:
        print(y,end="")
    print()
