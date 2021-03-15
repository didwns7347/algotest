n,m=map(int,input().split())
p=[x for x in range(n+1)]
def union(x,y):
    x=find(x)
    y=find(y)
    p[y]=x

def find(x):
    if x==p[x]:
        return x
    else:
        p[x]=find(p[x])
        
        return p[x]
        


for i in range(m):
    c,x,y=map(int,input().split())

    if c==0:
        union(x,y)
    else:
     
        if find(x)==find(y):
            print("YES")
        else:
            print("NO")
            
        
