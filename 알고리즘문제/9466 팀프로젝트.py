import sys
sys.setrecursionlimit(111111)
def find(x):
    global result
    check[x]=1
    cycle.append(x)
    if check[cho[x]]:
        if cho[x] in cycle:
            result+=cycle[cycle.index(cho[x]):]
        return
    else:
        find(cho[x])
for _ in range(int(input())):
    n=int(input())
    ans=0
    cho=list(map(int,input().split()))
    cho=[0]+cho[0:]
    check=[0 for _ in range(n+1)]
    result=[]
  
    for x in range(1,n+1):
        if check[x]==0:
            cycle=[]
            find(x)


    
    print(n-len(result))
            
            

