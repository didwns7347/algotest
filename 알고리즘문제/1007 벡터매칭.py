from itertools import combinations
def solve(ck):
    hx=0
    hy=0
    tx=0
    ty=0
    for x in range(n):
        if check[x]==1:
            hx+=pnt[x][0]
            hy+=pnt[x][1]
        else:
            tx+=pnt[x][0]
            ty+=pnt[x][1]
    return [hx-tx, hy-ty]
    


for _ in range(int(input())):
    pnt=[]
    n=int(input())
    for i in range(n):
        x,y=map(int,input().split())
        pnt.append([x,y])
    tmp=[x for x in range(n)]
    heads=list(combinations(tmp,len(tmp)//2))
    
    ans=float("inf")
    for h in heads:
        check=[0 for _ in range(n)]
        for i in h:
            check[i]=1
        answer=solve(check)
        answer=(answer[0]**2+answer[1]**2)**0.5            
        ans=min(ans,answer)
        
        
    print(ans)
    
               
