import sys
sys.setrecursionlimit(10000)
n=int(input())
m=list(map(int,input().split()))
dele=int(input())
tree=[[]for x in range(n)]
check=[0 for x in range(n)]
for x in range(0,n):
    if m[x]!= -1:
        tree[m[x]].append(x)
        tree[x].append(m[x])
    else:
        start=x

cnt=0
def dfs(a):
    global cnt
    if a==dele:
        return
    check[a]=1
    if len(tree[a])==1:
        cnt=cnt+1
    for x in tree[a]:
        if check[x]==0:
            dfs(x)
    return 1



dfs(start)
print(cnt)
