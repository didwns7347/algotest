
def solution(number,N):
    dp=[0 for x in range(number+1)]
    dp[1]=2
    dp[N]=1
    answer=0
    ans=10000
    for x in range(2,number+1):
        for y in range(1,x):
            if x==N:
                ans=1
                break
            tmp=dp[y]+dp[x-y]
            ans=min(ans,tmp)
        dp[x]=ans
        print(ans)
        ans=0
    answer=dp[number+1]
    return answer
print(solution(12,2))

                
            
