from collections import deque
def solution(n, edge):
    answer = 0
    q=deque()
    g=[[]for x in range(n+1)]
    dist=[0 for x in range(n+1)]
   
    for x in edge:
        g[x[0]].append(x[1])
        g[x[1]].append(x[0])
    q.append(1)
    
    while q:
        nd=q.popleft()
        for x in g[nd]:
            if dist[x]==0 and x != 1:
                dist[x]=dist[nd]+1
                q.append(x)
    maxdist=max(dist)
    print(dist)
    for x in dist:
        if x==maxdist:
            answer+=1
    return answer
a=6
b=[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

print(solution(a,b))