import sys
sys.setrecursionlimit(100000)
a=[" "] + list(input())
b=[" "] + list(input())
dp=[[0 for _ in range(len(b))] for _ in range(len(a))]

for x in range(1,len(a)):
    for y in range(1,len(b)):
        if b[y]==a[x]:
            dp[x][y]=dp[x-1][y-1]+1
        else:
            dp[x][y]=max(dp[x-1][y],dp[x][y-1])
out=[]
def find(x,y):
    
    if x==0 or y==0:
        return
    if dp[x][y]==dp[x-1][y]:
        return find(x-1,y)
    elif dp[x][y]==dp[x][y-1]:
        return find(x,y-1)
    elif dp[x][y]==dp[x-1][y-1]:
        return find(x-1,y-1)
    else:
        out.append(b[y])
        return find(x-1,y-1)

print(dp[-1][-1])
find(len(dp)-1,len(dp[0])-1)
out.reverse()
for x in out:
    print(x,end="")
