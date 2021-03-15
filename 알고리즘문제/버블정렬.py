def buble(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print(a)

def insert(a):
    n=len(a)
    for i in range(0,n-1):
        for j in range(i+1,n):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    print(a)
    
def selction(a):
    n=len(a)
    for i in range(0,n):
        tmp=a[i]
        idx=i
        for j in range(i+1,n):
            if tmp>a[j]:
                idx=j
                tmp=a[j]
        a[i],a[idx]=a[idx],a[i]
    print(a)
a=[9,8,7,6,5,4,3,2,1]

def part(arr,l,r):
    p=arr[r-1]
    idx=l-1
    
    for i in range(l,r-1):
        if arr[i]<p:
            idx+=1
            arr[idx],arr[i]=arr[i],arr[idx]
    arr[idx+1],arr[r-1]=arr[r-1],arr[idx+1]
    return idx+1
            
def quick(arr , l ,r):
    print(arr[l:r+1])
    if l<r:
        p=part(arr,l,r)
        quick(arr,l,p)
        quick(arr,p+1,r)
quick(a,0,len(a))
print(a)
