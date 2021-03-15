
for _ in range(int(input())):
    n,m=map(int,input().split())
    board=[[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        tmp=list(input())
        for j in range(m):
            if tmp[j]=="x":
                board[i][j]=1
    for x in board:
        print(x)
