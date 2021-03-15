from sys import stdin
input = stdin.readline
N=int(input())
num=[0,0,0]
dp=[0,0,0]
mdp=[0,0,0]
for x in range(N):
    num[0],num[1],num[2]=map(int,input().split())
    if x==0:
        dp[0],dp[1],dp[2]=num[0],num[1],num[2]
        mdp[0],mdp[1],mdp[2]=num[0],num[1],num[2]
    
        continue
    tmp0=max(dp[0],dp[1])+num[0]
    tmp1=max(dp)+num[1]
    tmp2=max(dp[1],dp[2])+num[2]
    dp=[tmp0,tmp1,tmp2]
    
    tmp0=min(mdp[0],mdp[1])+num[0]
    tmp1=min(mdp)+num[1]
    tmp2=min(mdp[1],mdp[2])+num[2]
    mdp=[tmp0,tmp1,tmp2]



print(max(dp),min(mdp))
