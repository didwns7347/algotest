import copy
n,m=map(int,input().split())
board=[]
rn=0
rm=0
bn=0
bm=0
hn=0
hm=0
for x in range(n):
    board.append(list(input()))
for x in range(n):
    for y in range(m):
        if board[x][y]=="R":
            rn=x
            rm=y
        if board[x][y]=="B":
            bn=x
            bm=y
        if board[x][y]=="O":
            hn=x
            hm=y
            
ans=11
def left(b,n):
    print("left")
    board=copy.deepcopy(b)
    global rm,bm,rn,bn,ans
    while True:
        if board[rn][rm-1]=="#" and board[bn][bm-1]=='#':
            break
        if board[bn][bm-1]=="O":
            return board
        if board[rn][rm-1]==".":
            board[rn][rm-1],board[rn][rm]=board[rn][rm],board[rn][rm-1]
            rm-=1
        if board[bn][bm-1]==".":
            board[bn][bm],board[bn][bm-1]=board[bn][bm-1],board[bn][bm]
            bm-=1
        if board[rn][rm-1]=="#" and board[bn][bm-1]=="R" or  board[rn][rm-1]=="B" and board[bn][bm-1]=="#":
            break
        if board[rn][rm-1]=="O":
            ans=min(ans,n+1)
            return board
    return board
def right(b,n):
    print("r")
    board=copy.deepcopy(b)
    global rm,bm,rn,bn,ans
    while True:
        if board[rn][rm+1]=="#" and board[bn][bm+1]=='#':
            break
        if board[bn][bm+1]=="O":
            return board
        if board[rn][rm+1]==".":
            board[rn][rm+1],board[rn][rm]=board[rn][rm],board[rn][rm+1]
            rm+=1
        if board[bn][bm+1]==".":
            board[bn][bm],board[bn][bm-1]=board[bn][bm-1],board[bn][bm]
            bm+=1
        if board[rn][rm+1]=="#" and board[bn][bm+1]=="R" or  board[rn][rm+1]=="B" and board[bn][bm+1]=="#":
            break
        if board[rn][rm+1]=="O":
            ans=min(ans,n)
            return board
    return board
def up(b,n):
    print("u")
    board=copy.deepcopy(b)
    global rm,rn,bm,bn,ans
    while True:
        if board[rn-1][rm]=="#" and board[bn-1][bm]=="#":
            break
        
        if board[rn-1][rm]=="#" and board[bn-1][nm]=="O":
            return board
        if board[rn-1][rm]==".":
            board[rn-1][rm],board[rn][rm]=board[rm][rn],board[rn-1][rm]
            rn-=1
        if board[bn-1][bm]==".":
            board[bn-1][bn],board[bn][bm]=board[bn][bm],board[bn-1][bm]
            bn-=1
            
        if board[bn-1][bm]=="#" and board[rn-1][rm]=="B" or board[rn-1][rm]=="#" and board[bn-1][bm]=="R":
            break
        if board[rn-1][rm]=="O":
            ans=min(ans,n+1)
            return board
    return board
def dwon(b,n):
    print("d")
    board=copy.deepcopy(b)
    global rm,rn,bm,bn,ans
    while True:
        if board[rn+1][rm]=="#" and board[bn+1][bm]=="#":
            break
        
        if board[rn+1][rm]=="#" and board[bn+1][nm]=="O":
            return board
        if board[rn+1][rm]==".":
            board[rn+1][rm],board[rn][rm]=board[rm][rn],board[rn+1][rm]
            rn+=1

        if board[bn+1][bm]==".":
            board[bn+1][bn],board[bn][bm]=board[bn][bm],board[bn+1][bm]
            bn+=1
            
        if board[bn+1][bm]=="#" and board[rn+1][rm]=="B" or board[rn+1][rm]=="#" and board[bn+1][bm]=="R":
            break
        if board[rn+1][rm]=="O":
            ans=min(ans,n+1)
            return board
    return board
        

        
def do(b,n):
    print(n)
    for x in b:
        print(x)
    if n==10:
        return
    do(left(b,n+1),n+1)
    do(right(b,n+1),n+1)
    do(up(b,n+1),n+1)
    do(dwon(b,n+1),n+1)
            
do(board,0)
