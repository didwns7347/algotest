n=int(input())

while n>0:
    num=int(input())
    dp=[0 for x in range(num)]
    if num>5:
        dp[0],dp[1],dp[2]=1,1,1
        dp[3]=2
        dp[4]=2
        for x in range(5,num):
            dp[x]=dp[x-1]+dp[x-5]
        print(dp[num-1])
        
    else:
        if num<4:
            print(1)
        else:
            print(2)
    n-=1
            
