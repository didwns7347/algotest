import sys
sys.setrecursionlimit(10000)
board=[[],[],[],[],[],[],[],[],[]]
blank=[]
for i in range(9):
    tmp=list(input())
 
    for x in range(9):
        if int(tmp[x])==0:
            blank.append([i,x])
        board[i].append(int(tmp[x]))

def BF(a,b,i):
 
   
    for num in range(1,10):
        if check(a,b,num):
            board[a][b]=num
            if i+1==len(blank):
                for x in range(9):
                    for y in range(9):
                        print(board[x][y],end="")
                    print()
                sys.exit()
            BF(blank[i+1][0],blank[i+1][1],i+1)
            board[a][b]=0
def check(x,y,num):
    for i in range(9):
        if board[x][i]==num and i != y:
            return False
        if board[i][y]==num and i !=x :
            return False
    xs=x//3
    ys=y//3
    for i in range(3*xs,3*(xs+1)):
        for j in range(3*ys,3*(ys+1)):
            if x==i and j==y:
                continue
            if board[i][j]==num:
                return False
    return True
BF(blank[0][0],blank[0][1],0)
