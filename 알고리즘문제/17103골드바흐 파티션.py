n=int(input())
num=[1 for x in range(1000001)]
ss=[]
num[0]=0
num[1]=0
for x in range(2,1000001//2):
    if num[x]:
        ss.append(x)
        for y in range(2,1000001):
            if x*y>1000000:
                break
            num[x*y]=0

for x in range(n):
    cnt=0
    k=int(input())
    for x in ss:
        if k-x<=0 or x*2>k:
            break
        if num[k-x]:
            cnt+=1
    print(cnt)
    
