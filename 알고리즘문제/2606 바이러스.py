
n=int(input())
parent=[x for x in range(n+1)]
m=int(input())
def union(x,y):
    x=find(x)
    y=find(y)
    if x != y:
        parent[y]=x

def find(x):
    if x==parent[x]:
        return x
    else:
        parent[x]=find(parent[x])
        return parent[x]
for i in range(m):
    x,y=map(int,input().split())
    union(x,y)



cnt=0
for x in range(2,n+1):
    if find(x)==find(1):
        cnt+=1
print(cnt)
