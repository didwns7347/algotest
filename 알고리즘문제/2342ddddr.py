step = list(map(int,input().split()))

dp=[[0 for _ in range(len(step))] for _ in range(2)]
zero=[[0 for _ in range(2)] for _ in range(len(step))]
one=[[0 for _ in range(2)] for _ in range(len(step))]
   
#0 왼발 1오른발
dp[0][0]=2
zero[0][0]=step[0]
zero[0][1]=0
dp[0][1]=2
one[0][0]=0
one[0][1]=step[0]

for i in range(1, len(step)-1):
    if step[i]==1:
        
    elif step[i]==2:
    elif step[i]==3:
    elif step[i]==4
        



    
