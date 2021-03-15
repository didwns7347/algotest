import sys
n=int(input())
a=[0]
for x in range(n):
    a.append(int(sys.stdin.readline().strip()))

for i in range(1,len(a)):
    change=False
    for j in range(1,len(a)-i):
        if a[j]>a[j+1]:
            change = True
            a[j],a[j+1]=a[j+1],a[j]
    if change==False:
        print(i)
        break
    print(a)
