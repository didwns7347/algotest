import copy
def solution(key, lock):
    for _ in range(4):
        key=list(zip(*key[::-1]))
        if check(key,lock):
            return True
        
    
    return False
def check(k,l):
    size=len(k)+len(l)+len(k)-2
    board=[[0 for x in range(size)] for y in range(size)]
    for x in range(size):
        for y in range(size):
            if x>=len(k)-1 and x<len(k)+len(l)-1 and y>=len(k)-1 and y<len(k)+len(l)-1:
                board[x][y]=l[x-len(k)+1][y-len(k)+1]

    for x in range(size-len(k)+1):
        for y in range(size-len(k)+1):
            b=go(x,y,board,k)
            if check_open(b,len(key)-1,len(l)):
                return True
    return False
def go(x,y,b,k):
    board=copy.deepcopy(b)
    for i in range(x,x+len(k)):
        for j in range(y,y+len(k)):
            board[i][j]=board[i][j]+k[i-x][j-y]
    return board
def check_open(b,h,w):

    for x in range(h,h+w):
        for y in range(h,h+w):
            if b[x][y]!=1:
                return False
    return True
key=[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock=[[1, 1, 1], [1, 1, 0], [1, 0, 1]]

print(solution(key,lock))