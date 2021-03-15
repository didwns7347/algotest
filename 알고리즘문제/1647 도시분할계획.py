from sys import stdin


g=[]
input = stdin.readline
n,m=map(int, input().split())

for _ in range(m):
    a,b,c=map(int,input().split())
    g.append([c,a,b])
    g.append([c,b,a])
g.sort()
    
    
ans=0
cnt=0
parent=[x for x in range(n+1)]
def union(a,b):
    sa=find(a)
    sb=find(b)
    if sa == sb:
        return False
    if sa < sb:
        parent[sa]=sb
    else:
        parent[sb]=sa
    return True
def find(a):
    if a==parent[a]:
        return a
    tmp=find(parent[a])
    parent[a]=tmp
    return tmp

for c,a,b in g:
    if union(a,b):
        if cnt==n-2:
            break
        ans+=c
        cnt+=1
   
    
print(ans)
