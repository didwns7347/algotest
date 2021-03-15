word=list(input())

n=len(word)
board=[ [0 for _ in range(len(word))] for _ in range(len(word))]
answer=float("inf")
def check(s,f):
    while True:
        if s>=f:
            break
        if word[s]!=word[f]:
            return False
        s+=1
        f-=1
    return True
for i in range(n):
    for j in range(i,n):
        if check(i,j):
            board[i][j]=1
dp=[0 for x in range(n)]

        
for i in range(0,n):
    for j in range(0,i+1):
        if board[j][i]==1:
            if dp[i]==0 or dp[j-1]+1 <dp[i]:
                dp[i]=dp[j-1]+1
print(dp[n-1])
