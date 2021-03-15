n=int(input())
num=list(map(int,input().split()))

num.sort()
ans=float("inf")



for x in range(0,n-2):
    l=x+1
    r=n-1
    while True:
        if ans>abs(num[x]+num[l]+num[r]):
            ans=abs(num[x]+num[l]+num[r])
            out=[x,l,r]

        if l==r-1:
            break
        if num[x]+num[l]+num[r]<0:
            l+=1
        else:
            r-=1
        
print(num[out[0]],num[out[1]],num[out[2]])


        
            
        
