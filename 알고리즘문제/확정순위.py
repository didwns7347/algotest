from collections import deque
def solution(n, results):
    pc=[ [0,0] for _ in range(n+1)]
    answer=0
    parent=[[] for _ in range(n+1)]
    child=[[] for _ in range(n+1)]
    
    for a,b in results:
        parent[b].append(a)
        child[a].append(b)
    for i in range(1,n+1):
        pc[i][0]=check(i,parent,n+1)
        pc[i][1]=check(i,child,n+1)
        if pc[i][0]+pc[i][1]==n-1:
            answer+=1
    for x in pc:
        print(x)

    print(answer)
    return answer
def check(i,link,limit):
    q=deque()
    q.append(i)
    check=[0 for _ in range(limit)]
    check[i]=1
    while q :
        now=q.popleft()
        for nxt in link[now]:
            if check[nxt]==0:
                check[nxt]=1
                q.append(nxt)
    return sum(check)-1
a=5
b=[[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]	
solution(a,b)
a=8
b= [[1, 2], [2, 3], [3, 4],[5, 6], [6, 7], [7, 8]] 
solution(a,b)
