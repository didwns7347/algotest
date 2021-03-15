import sys
from collections import deque
q=deque()
n=int(input())
t=[]
tree=[[] for x in range(n)]
check[[0,0] for x in range(n)]
for x in range(n):
    tmp=list(map(str,sys.stdin.readline().strip().split()))
    t.append(tmp)
for x in t:
    tree[ord(x[0])-65].append(x[1])
    tree[ord(x[0])-65].append(x[2])
def dfs(tmp):
    if x in range(1,3):
        if tmp[x]!="." and check[ord[tmp[0]-65][x]==0
                                
        dfs(tmp[ord[tmp[x]-65)])
    else:
        return print(tmp[0])

q.append(tree[0])
while True:
    if not q:
        break
    tmp=q.popleft()
    for x in range(2):
        if 
