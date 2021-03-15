def solution(N, stages):
    answer = []
    chel=[0 for x in range(N+2)]
    clear=[0 for x in range(N+2)]
    for x in stages:
        chel[x]+=1
        for i in range(1,x):
            clear[i]+=1
    print(clear)
    out=[]
    for x in range(1,len(chel)):
        if chel[x]!=0:
            tmp=[x,chel[x]//clear[x]]
            out.append(tmp)
    
    print(out)
    return answer
print(solution(5,[2,1,2,6,2,4,3,3]))