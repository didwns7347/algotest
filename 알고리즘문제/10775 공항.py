import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
g=int(input())
p=int(input())

fly=[]
parent=[x for x in range(g+1)]
def find(x):
    if parent[x]==x:
        return x
    tmp=find(parent[x])
    parent[x]=tmp
    return tmp

    

ans=0
for _ in range(p):
    fly.append(int(input()))
for x in range(p):
    w=find(fly[x])
    if w==0:
        break
    parent[w]=w-1
    ans+=1
print(ans)
print(parent)
