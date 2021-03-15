h,w=map(int,input().split())
board=[]
for x in range(h):
    board.append(list(map(int,input().split())))
one=[[[0,0],[0,1],[0,2],[0,3]],[[0,0],[1,0],[2,0],[3,0]]]
two=[[[0,0],[0,1],[1,0],[1,1]]]
three=[[[0,0],[0,1],[0,2],[1,0]],
       [[0,0],[0,1],[0,2],[1,2]],
       [[0,0],[1,0],[1,1],[1,2]],
       [[1,0],[1,1],[1,2],[0,2]],
       [[0,0],[1,0],[2,0],[0,1]],
       [[0,0],[1,0],[2,0],[2,1]],
       [[0,0],[0,1],[1,1],[2,1]],
       [[0,1],[1,1],[2,1],[2,0]]]
four=[[[0,0],[1,0],[1,1],[2,1]],
      [[0,1],[1,0],[1,1],[2,0]],
      [[0,1],[0,2],[1,0],[1,1]],
      [[0,0],[0,1],[1,1],[1,2]]]

five=[[[0,0],[0,1],[0,2],[1,1]],
      [[0,0],[1,0],[1,1],[2,0]],
      [[0,1],[1,0],[1,1],[1,2]],
      [[0,1],[1,1],[1,0],[2,1]]]

def calc(a,b):
    ans=0
    for x in one:
        tmp=0
        for y in x:
            if a+y[0]>=0 and a+y[0]<h and b+y[1]>=0 and b+y[1]<w:
                tmp+=board[a+y[0]][b+y[1]]
            else:
                tmp=0
        ans=max(tmp,ans)
    for x in two:
        tmp=0
        for y in x:
            if a+y[0]>=0 and a+y[0]<h and b+y[1]>=0 and b+y[1]<w:
                tmp+=board[a+y[0]][b+y[1]]
            else:
                tmp=0
        ans=max(tmp,ans)
    for x in three:
        tmp=0
        for y in x:
            if a+y[0]>=0 and a+y[0]<h and b+y[1]>=0 and b+y[1]<w:
                tmp+=board[a+y[0]][b+y[1]]
            else:
                tmp=0
        ans=max(tmp,ans)
    for x in four:
        tmp=0
        for y in x:
            if a+y[0]>=0 and a+y[0]<h and b+y[1]>=0 and b+y[1]<w:
                tmp+=board[a+y[0]][b+y[1]]
            else:
                tmp=0
        ans=max(tmp,ans)
    for x in five:
        tmp=0
        for y in x:
            if a+y[0]>=0 and a+y[0]<h and b+y[1]>=0 and b+y[1]<w:
                tmp+=board[a+y[0]][b+y[1]]
            else:
                tmp=0
        ans=max(tmp,ans)
    return ans
        

def solve(m):
    ans=0
    for x in range(h):
        for y in range(w):
            ans=max(calc(x,y),ans)
    return ans
print(solve(board))
