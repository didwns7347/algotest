n=int(input())
uf=[x for x in range(n)]

cnum=int(input())
cities=[]
def union(x,y):
    x=find(x)
    y=find(y)
    if x!=y:
        uf[y]=x
def find(x):
    if x==uf[x]:
        return x
    else:
        t=find(uf[x])
        uf[x]=t
        return t
for x in range(n):
    cities.append(list(map(int,input().split())))
plan=list(map(int,input().split()))

for x in range(n):
    for y in range(n):
        if cities[x][y]==1:
            union(x,y)
        
out=[]
fin=False
for x in range(len(plan)-1):
    if uf[plan[x]-1]!=uf[plan[x+1]-1]:
        print("NO")
        fin=True
        break
if not fin:
    print("YES")