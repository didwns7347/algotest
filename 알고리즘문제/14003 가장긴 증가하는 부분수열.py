n=int(input())

num=list(map(int,input().split()))

c=[float("inf") for _ in range(n+1)]
c[1]=num[0]

alist=[[]for _ in range(n+1)]
c[0]=-float("inf")

alist[1].append(num[0])
cnt=1
def find(s,f,tg):
    mid =(s+f)//2
    if s==f:
        return s
    elif s+1==f:
        if c[s]>=tg:
            return s
        else:
            return f
    
    if c[mid]==tg:
        return mid
    
    elif c[mid]<tg:
        return find(mid+1,f,tg)


    else:
        return find(s,mid,tg)
    
ans=[0]
for i in range(1,n):
    number=num[i]
   
    if c[cnt]<number:
        cnt+=1
        c[cnt]=number
        ans.append(cnt-1)
     
    else:
        tmp=find(0,cnt,number)
        c[tmp]=number
        ans.append(tmp-1)

print(cnt)
print(ans)
out=[]
for i in range(len(ans)-1,-1,-1):
    if ans[i]==cnt-1:
        out.append(num[i])
        cnt-=1
print(*out[::-1])
    
    

print(c)
print(out)
