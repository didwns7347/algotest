inp=input()
tree=[False for _ in range(len(inp)+1)]
def go(st,idx):
    print(st)
    if len(st)<3:
        return
    if len(st)==5 and st[0]=="(" and st[-1]==")":
        tree[idx]=st[2]
        tree[idx*2]=st[1]
        tree[idx*2+1]=st[3]
        return
    if len(st)==3:
        tree[idx]=st[1]
        tree[idx*2]=st[0]
        tree[idx*2+1]=st[2]
        return
        
    stack=[]
    tmp=""
    for x in range(len(st)):
        tmp+=st[x]
        if st[x]=="(":
            if tmp and not stack and x!=0:
                tree[idx*2]=st[0:x-1]
                tree[idx]=st[x-1]
                tree[idx*2+1]=st[x:]
                go(tree[idx*2],2*idx)
                go(tree[idx*2+1],2*idx+1)
                return
            stack.append(0)
        elif st[x]==")":
            stack.pop()
            if not stack and x!=len(st)-1:
                print("tmp= ",tmp)
                tree[idx*2]=st[0:x+1]
                tree[idx]=st[x+1]
                tree[idx*2+1]=st[x+2:]
                go(tree[idx*2],2*idx)
                go(tree[idx*2+1],2*idx+1)
                return
            if not stack and x==len(st)-1:
                print("this)")
                go(st[1:x],idx)
                return
def postorder(idx):
    if tree[idx*2]:
        postorder(idx*2)
    if tree[idx*2+1]:
        postorder(idx*2+1)
    print(tree[idx],end="")
    
                
go(inp,1)
postorder(1)
                
            
