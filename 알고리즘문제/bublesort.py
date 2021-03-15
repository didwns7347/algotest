a=[8,9,4,5,3,2,1]

for x in range(0,len(a)):
    for y in range(x+1,len(a)):
        if a[x]>a[y]:
            tmp=a[x]
            a[x]=a[y]
            a[y]=tmp

print(a)
