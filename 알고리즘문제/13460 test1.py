import copy
n,m=map(int,input().split())
board=[]
ans=100
#lrud

#0서 1동 2북 3남
my=[-1,1,0,0]
mx=[0,0,-1,1]
for x in range(n):
    board.append(list(input()))

for x in range(n):
    for y in range(m):
        if board[x][y]=="B":
            bn=x
            bm=y
        if board[x][y]=="R":
            rn=x
            rm=y
        if board[x][y]=="O":
            on=x
            om=y
def move(board,c,n):
    global bn,bm,rn,rm,on,om,ans
    cnt=0
    while True:
        if cnt==n:
            break
        if board[bn+mx[c]][bm+my[c]]==".":
            board[bn][bm],board[bn+mx[c]][bm+my[c]]=board[bn+mx[c]][bm+my[c]],board[bn][bm]
            bn+=mx[c]
            bm+=my[c]
        if board[rn+mx[c]][rm+my[c]]==".":
            board[rn][rm],board[rn+mx[c]][rm+my[c]]=board[rn+mx[c]][rm+my[c]],board[rn][rm],
            rm+=my[c]
            rn+=mx[c]
        if  board[rn+mx[c]][rm+my[c]]=="O":
            ans=min(ans,n)
            break
        cnt+=1
        

    return board

def do(board,n):
   
    if n>=10 :
        return 
   
    tmp=copy.deepcopy(board)
    do(move(tmp,0,n+1),n+1)
    tmp=copy.deepcopy(board)
    do(move(tmp,1,n+1),n+1)
    tmp=copy.deepcopy(board)
    do(move(tmp,2,n+1),n+1)
    tmp=copy.deepcopy(board)
    do(move(tmp,3,n+1),n+1)


do(board,0)
       
print(ans)
