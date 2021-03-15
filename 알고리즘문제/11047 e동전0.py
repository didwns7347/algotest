import sys
coin=[]

n,k= map(int, input().split())

for x in range(n):
    tmp=int(sys.stdin.readline())
    coin.append(tmp)

cnt=len(coin)-1
count=0
while True:

    if k==0:
        break
    if k//coin[cnt]>0:
        count+=k//coin[cnt] 
        k=k%coin[cnt]
       
    else:
        cnt-=1
print(count)
