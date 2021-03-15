n=int(input())
a=map(int,input().split())
a=list(a)
cnt=0
num=[1 for x in range(0,1001)]

for i in range(2,501):
    if num[i]:
        for j in range(2,1001):
            if i*j>1000:
                break
            num[i*j]=0
        
for x in a:
    if num[x]!=0 and x>1:
        cnt+=1

print(cnt)
