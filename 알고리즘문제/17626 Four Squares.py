n=int(input())
num=[x for x in range(n+1)]
tmp=1
while True:
    if tmp*tmp>n:
        break
    num[tmp*tmp]=1
    tmp+=1
num[1]=1
num[2]=2
num[3]=3
num[5]=2
for x in range(6,n+1):
    for y in range(1,n):
        if y*y>x:
            break
        num[x]=min(num[x],num[x-y*y]+num[y*y])
print(num[n])
