n,m,k = map(int,input().split())
card=list(map(int,input().split()))
draw=list(map(int,input().split()))
check=[0 for _ in range(n+1)]
def find(node):
    if check[node]==0:
        check[node]=1
        return node
    return find(node+1)
for num in draw:
    print(find(num+1))
