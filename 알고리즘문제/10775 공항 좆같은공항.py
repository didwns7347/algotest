import sys
g=int(sys.stdin.readline())
p=int(sys.stdin.readline())
plane=[]

for _ in range(p):
    plane.append(int(sys.stdin.readline()))

def find(x):
    if x==parent[x]:
        return x
    p=find(parent[x])
    parent[x]=p
    return parent[x]

def union(x,y):
    x=find(x)
    y=find(y)
    parent[x]=y

parent = {i:i for i in range(g+1)}
cnt=0
for i in plane:
    x=find(i)
    if x==0:
        break
    union(x,x-1)
    cnt+=1
print(cnt)
