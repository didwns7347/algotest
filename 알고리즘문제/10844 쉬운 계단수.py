n=int(input())

a=[[0 for x in range(10)] for y in range(n)]
a[0]=[0,1,1,1,1,1,1,1,1,1]
for x in range(1,n):
    for y in range(10):
        if y==0:
            a[x][y+1]=a[x-1][y]+a[x][y+1]
        elif y==9:
            a[x][y-1]=a[x-1][y]+a[x][y-1]
        else:
            a[x][y-1]=a[x-1][y]+a[x][y-1]
            a[x][y+1]=a[x-1][y]+a[x][y+1]
print(sum(a[n-1])%1000000000)
