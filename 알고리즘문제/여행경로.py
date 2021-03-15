import heapq
bd=[[] for _ in range(100001)]
def ford(parent,root,mid):
    print(root,mid)
    global bd
    tmp=root
    while True:
        tmp-=1
        if bd[root]:
            break
        if tmp==0:
            break
    print(tmp)
    while bd[tmp]:
        nxt=heapq.heappop(bd[tmp])
        if nxt<mid:
            ford(mid,tmp,nxt)
        if parent!=0:
            if nxt > parent:
                heapq.heappush(bd[tmp],nxt)
                break
            else:
                ford(mid,tmp,nxt)
                break
    return
                
def solution(nodeinfo):
    global bd
    answer = [[]]
    cnt=1
    for a,b in nodeinfo:
        heapq.heappush(bd[b],a)
    print(bd[5])
    
    nodeinfo.sort(key=lambda x:x[1],reverse=True)
    for a,b in nodeinfo:
        bd[a].append(b)
        
    ford(0,nodeinfo[0][1],nodeinfo[0][0])
    return answer

solution([[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]])

            
