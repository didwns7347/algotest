import sys
n, m = map(int,input().split())
answer=n+1
num=list(map(int, input().split()))
dp=[0 for _ in range(n)]
dp[0]=num[0]
for x in range(1,n):
    dp[x]=dp[x-1]+num[x]
if dp[0]>=m:
    print(1)
    sys.exit()

for x in range(n):
    if dp[x]>m:
        for y in range(x-1,-1,-1):
            if x-y>answer:
                break
            if dp[x]-dp[y]>=m:
                if answer>x-y:
                    answer=x-y
                    break
                else:
                    break
    if dp[x]==m:
        answer=x+1
if answer>n:
    print(0)
else:
    print(answer)
