case=int(input())

out=[]
def union(a,b,cnt):
    a=find(a)
    b=find(b)
    if a!=b:
        friends[b]=a
        cnt[a]+=cnt[b]
def find(a):
    if friends[a]==a:
        return a
    else:
        tmp=find(friends[a])
        friends[a]=tmp
        return tmp
def findp(a):
    if friends[a]==a:return a
    return findp(friends[a])

for x in range(case):
    n= int(input())
    friends={}
    cnt={}
    for i in range(n):
        a,b=input().split()
        if a not in friends:
            friends[a]=a
            cnt[a]=1
        if b not in friends:
            friends[b]=b
            cnt[b]=1
        union(a,b,cnt)
        
        out.append(cnt[findp(a)])
        
   
for x in out:
    print(x)