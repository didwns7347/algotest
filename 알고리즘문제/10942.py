import sys
input= sys.stdin.readline

n=int(input())
word=list(map(int,input().split()))
def check(s,f):
    while True:
        if s>=f:
            break
        if word[s]!=word[f]:
            return False
        s+=1
        f-=1
    return True
board=[[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(i,n):
        if check(i,j):
            board[i][j]=1
m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    if board[a-1][b-1]==1:
        print(1)
    else:
        print(0)
