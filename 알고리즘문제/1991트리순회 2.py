n= int(input())
tree=[[] for x in range(26)]
check=[0 for x in range(26)]
for x in range(n):
    a,b,c=input().split()
    tree[ord(a)-65].append(b)
    tree[ord(a)-65].append(c)



def pre(a):
    check[a]=1
    print(chr(a+65),end="")
    if tree[a][0]=="." and tree[a][1]==".":
        return
    if tree[a][0]!="." and check[ord(tree[a][0])-65]==0:
        pre(ord(tree[a][0])-65)
    if tree[a][1]!="." and check[ord(tree[a][1])-65]==0:
        pre(ord(tree[a][1])-65)

pre(0)
check=[0 for x in range(26)]    

def inord(a):
    check[a]=1
    if tree[a][0]=="." and tree[a][1]==".":
        print(chr(a+65),end="")
        return
    if tree[a][0]!="." and check[ord(tree[a][0])-65]==0:
        inord(ord(tree[a][0])-65)
    print(chr(a+65),end="")
    if tree[a][1]!="." and check[ord(tree[a][1])-65]==0:
        inord(ord(tree[a][1])-65)
print()
inord(0)
check=[0 for x in range(26)]

def post(a):
    
    check[a]=1
    if tree[a][0]=="." and tree[a][1]==".":
        print(chr(a+65),end="")
        return
    if tree[a][0]!="." and check[ord(tree[a][0])-65]==0:
        post(ord(tree[a][0])-65)
    if tree[a][1]!="." and check[ord(tree[a][1])-65]==0:
        post(ord(tree[a][1])-65)
    print(chr(a+65),end="")
print()
post(0)

