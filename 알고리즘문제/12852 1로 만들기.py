n=int(input())
dp = [x  for x in range(1000001)]
dp[1]=0
dp[2]=1
dp[3]=1

    
for x in range(4,n+1):
    if x%2==0 and x%3==0:
        dp[x]=min(dp[x-1],dp[x//2],dp[x//3])+1
    elif x%2==0:
        dp[x]=min(dp[x-1],dp[x//2])+1
    elif x%3==0:
        dp[x]=min(dp[x-1],dp[x//3])+1
    else:
        dp[x]=dp[x-1]+1
    
print(dp[n])        
out=[]
while True:
    out.append(n)
    if n==1:
        break
    
    if n%2==0 and n%3==0:
        if dp[n-1]==min(dp[n-1],dp[n//2],dp[n//3]):
            n=n-1
            
        elif dp[n//2]==min(dp[n-1],dp[n//2],dp[n//3]):
            n=n//2
           
        else:
            n=n//3
            
    elif n%2==0:
        if dp[n-1]==min(dp[n-1],dp[n//2]):
            n=n-1
            
        elif dp[n//2]==min(dp[n-1],dp[n//2]):
            n=n//2
       
            
    elif n%3==0:
        if dp[n-1]==min(dp[n-1],dp[n//3]):
            n=n-1
      
           
        else:
            n=n//3
            
    else:
        n=n-1

for x in out:
    print(x,end=" ")
