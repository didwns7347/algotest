def solution(gems):
    check=list(set(gems))
    c=[]
    ans=[]
    s=0
    for x in range(len(gems)):
        if gems[x] not in c:
            c.append(gems[x])
        if len(c)==len(check):
            ans.append([s,x,x-s])
            s=x
            c=[]
    
    ans.sort( key = lambda x : (x[2], x[0]))
    print(ans)
    answer = [ans[0][0],ans[0][1]]
    return answer
gems=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems))
