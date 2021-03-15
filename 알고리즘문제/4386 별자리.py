import heapq
n=int(input())
star=[]
parent=[x for x in range(n)]
for _ in range(n):
    a,b=map(float,input().split())
    star.append([a,b])
road=[]
def union(a,b):
    na=find(a)
    nb=find(b)
    if na==nb:
        return False
    elif na<nb:
        parent[nb]=na
    else:
        parent[na]=nb
    return True
def find(a):
    if parent[a]==a:
        return a
    tmp=find(parent[a])
    parent[a]=tmp
    return tmp
    
for i in range(n):
    for j in range(i+1,n):
        if i==j:
            continue
        a=star[i][0]-star[j][0]
        b=star[i][1]-star[j][1]
        dist=(a**2+b**2)**0.5
        heapq.heappush(road,[dist,i,j])

cnt=0
ans=0
while True:
    c,a,b=heapq.heappop(road)
    if union(a,b):
        cnt+=1
        ans+=c
    if cnt==n-1:
        print(round(ans,2))
        break
        
        
