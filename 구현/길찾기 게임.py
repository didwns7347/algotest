def solution(nodeinfo):
    q=[[] for x in range(len(nodeinfo))]
    for x,node in enumerate(nodeinfo):
        node.append(x+1)
        q[node[1]].append(node)
    for x in q:
        if x:
            x.sort()
    for x in q:
        if x:
            print(x)
        
    answer = [[]]
    return answer
node=[[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
solution(node)
