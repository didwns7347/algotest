import sys

n=int(input())
t=[]
out=[]
check=[[0,0] for x in range(n)]
tree=[[] for x in range(n)]
for x in range(n):
    tmp=list(map(str,sys.stdin.readline().strip().split()))
    t.append(tmp)
for x in t:
    tree[ord(x[0])-65].append(x[1])
    tree[ord(x[0])-65].append(x[2])

def post(tr):
    for x in range(2):
        if tr[x]!=".":
            out.append(tr[x])
            dfs(tree[ord(tr[x])-65])
    
    return print(out.pop(),end='')

def pre(tr):
    for x in range(2):
        if tr[x]!=".":
            out.append(tr[x])
            dfs(tree[ord(tr[x])-65])
    
    return print(out.pop(),end='')

out.append('A')
post(tree[0])
print()
out=[]
out.append('A')
pre(tree[0])


