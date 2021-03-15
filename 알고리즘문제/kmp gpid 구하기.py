st=list(input())
dp=[ 0 for _ in range(len(st))]
i=-1
j=0
dp[j]=i
while (j<len(st)):
    if i==-1 or i>=0 and st[i]==st[j]:
        i+=1
        j+=1
        dp[j]=i
    else: i=dp[i]

print(dp)
