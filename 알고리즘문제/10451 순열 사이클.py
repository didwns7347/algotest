import sys
sys.setrecursionlimit(10000)
n=int(input())
def dfs(a,b):

    check[a]=1
    if check[b]==0:
        dfs(b,case[b])
    return 1
for x in range(n):
    g=[]
    cnt=0
    num=int(input())
    check=[0 for x in range(num+1)]
    tmp=sys.stdin.readline().strip()
    case=list(map(int,tmp.split()))
    case=[0]+case
    test=[x for x in range(1,num+1)]

    for x in range(1,num+1):
        if check[x]==0:
            cnt+=dfs(x,case[x])
    print(cnt)
