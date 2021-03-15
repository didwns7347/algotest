n,k=map(int,input().split())
coin=[ int(input()) for x in range(n)]
dp=[[] for x in range(100001)]
money=[0 for x in range(100001)]
tmp=0
cnt=0
while True:
    if cnt==0:
        for x in coin:
            dp[cnt].append(x)
            money[x]=1
    else:
        for x in dp[cnt-1]:
            for y in coin:
                tmp=min(x+y,tmp)
                if x+y<100000 and money[x+y]==0:
                    dp[cnt].append(x+y)
                    money[x+y]=cnt+1
                elif x+y<100000 and money[x+y]!=0:
                    money[x+y]=min(money[x+y],cnt+1)
            if tmp>100000:
                break
    cnt+=1
    if cnt >=100001 or tmp>100000:
        break
if money[k]==0:
    print(-1)
else:
    print(money[k])
