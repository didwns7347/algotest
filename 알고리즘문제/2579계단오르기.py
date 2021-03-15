num = int(input())
a=[ int(input()) for x in range(num)]
s=[0 for x in range(num)]
s[0]=a[0]
s[1]=a[1]+a[0]
s[2]=max(a[2]+a[0],a[0]+a[1],a[1]+a[2])
for x in range(3,num):
    s[x]=max(a[x]+s[x-2],a[x]+a[x-1]+s[x-3])
print(s[num-1])
