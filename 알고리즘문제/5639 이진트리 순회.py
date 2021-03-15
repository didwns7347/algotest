tree=[[0,0,0] for x in range(10001)]
inp=[]
cnt=0
while True:
    n=input()
    if not n:
        break
    n=int(n)
    inp.append(n)
tree[0][0]=inp[0]
for x in range(1,len(inp)):
    if inp[x]<inp[x-1]:
        tree[x-1][1]=inp[x]
        tree[x][0]=inp[x]
    else:
        for y in range(x-1,-1,-1):
            if tree[y][0]>inp[x]:
                tree[y-1][2]=inp[x]
                break
    if inp[x]>tree[0][0]:
        tree
    

print("XXXXXX")
