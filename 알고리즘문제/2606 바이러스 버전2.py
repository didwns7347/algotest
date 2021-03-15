import sys
n=int(input())
cnt=0
out=[]
check=[0 for x in range(n+1)]
link=[[] for _ in range(n+1)]
m=int(input())
for x in range(m):
    a,b=map(int,sys.stdin.readline().split())
    link[a].append(b)
    link[b].append(a)

def dfs(n):
    global cnt
    check[n]=1
    for x in link[n]:
        if check[x]==0:
            out.append(x)
            dfs(x)
dfs(1) 
print(len(out))
