def solution(n, weak, dist):
    answer = 0
    sw=[ 0 for x in range(n)]
    
    for i,w in enumerate(weak):
        sw[w]=1
    bw=reversed(sw)
    cnt=0
    for x in range(n):
        if weak[x]==1 and cnt==0:
            cnt=1
            d=dist.pop()

    return answer