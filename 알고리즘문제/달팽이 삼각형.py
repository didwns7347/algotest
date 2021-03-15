def solution(n):
    answer = []
    board=[[0 for _ in range(n)] for _ in range(n)]
    cnt=0
    i,j=0,0
    fin=n*(n+1)//2
    op="dwon"
    while True:
        cnt+=1
        if op=="dwon":
            board[i][j]=cnt
            if i==n-1 or board[i+1][j]!=0:
                j+=1
                op="right"
            else:
                i+=1
        elif op=="right":
            board[i][j]=cnt
            if j==n-1 or board[i][j+1]!=0:
                op="up"
                i-=1
                j-=1
            else:
                j+=1
        elif op=="up":
            board[i][j]=cnt
            if board[i-1][j-1]!=0:
                op="dwon"
                i+=1
            else:
                i-=1
                j-=1
        if cnt==fin:
            break
    for x in board:
        for y in x:
            if y==0:
                continue
            answer.append(y)

    return answer

a=solution(6)
for x in a:
    print(a)
