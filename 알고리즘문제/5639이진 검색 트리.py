import sys
sys.setrecursionlimit(10000)

tree=[]
def postorder(start,fin):
    if start>fin:
        return
    tmp=fin+1
    for x in range(start+1,fin+1):
        if tree[x]>tree[start]:
            tmp=x
            break
    postorder(start+1,tmp-1)
    postorder(tmp,fin)
    return print(tree[start])
cnt=0        
while cnt<=10000:
    try:
        node=int(input())
        tree.append(node)
    except:
        break
    cnt+=1

postorder(0 ,len(tree)-1)


