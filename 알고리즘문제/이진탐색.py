import sys
m=[]
cnt=0
tree=[[-1,-1] for x in range(1000000)]
check=[0 for x in range(1000000)]
def post(n):
    check[n]=1
    if tree[n][0]!=-1 and check[tree[n][0]]==0:
        post(tree[n][0])
    if tree[n][1]!=-1 and check[tree[n][1]]==0:
        post(tree[n][1])
    if tree[n][0]==-1 and tree[n][1]==-1:
        print(n)
        return
    print(n)
        
    
    
while True:
    a=sys.stdin.readline().strip()
    if not a:
        break
    a= int(a)
    m.append(a)
    last=a
    if cnt!=0:
        last=m[len(m)-2]

    if a<last:
        tree[last][0]=a
    elif a>last:
        for x in range(len(m)-2,-1,-1):
            if a < m[x]:
                tree[m[x+1]][1]=a
                break
            if x==0:
                tree[m[x]][1]=a

    cnt+=1
for x in m:
    print(x,tree[x])

post(m[0]) 
