from collections import deque
grm=0
def solution(n, edges):
    board=[[] for _ in range(n+1)]
    answer=0
    for a,b in edges:
        board[a].append(b)
        board[b].append(a)
    start,fin=find(board,n)
    q=deque()
    q.append(start)
    dists=BFS(board,q,n,start)
    q=deque()
    q.append(fin)
    distf=BFS(board,q,n,fin)
    for i in range(1,n+1):
        if i==start or i==fin:
            continue
        print(start,i,fin,dists[i],distf[i],grm,dists[i]+distf[i]+grm)
        answer=max(answer,dists[i]+distf[i]+grm)
    print(start,fin)
    return answer//3
def find(bd,n):
    global grm
    q=deque()
    q.append(1)
    tmp=BFS(bd,q,n,1)
    print(tmp)
    start=tmp.index(max(tmp))
    q=deque()
    q.append(start)
    tmp=BFS(bd,q,n,start)
    grm=max(tmp)
    fin=tmp.index(grm)
    return start,fin
def BFS(bd,q,n,start):
    check=[-1 for _ in range(n+1)]
    check[start]=0
    while q:
        now=q.popleft()
        for nxt in bd[now]:
            if check[nxt]==-1:
                check[nxt]=check[now]+1
                q.append(nxt)
    return check
print(solution(4,[[1,2],[2,3],[3,4]]))
print(solution(12,[[1,2],[1,3],[2,4],[3,5],[3,6],[4,7],[4,8],[5,9],[5,10],[6,11],[6,12]]))
print(solution(5,[[1,5],[2,5],[3,5],[4,5]]))
