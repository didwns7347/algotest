from itertools import combinations
def solution(user_id, banned_id):
    answer=0
    ans=[]
    check=[0 for x in range(len(user_id))]
    for x in range(len(banned_id)):
        for y in range(len(user_id)):
            if comp(banned_id[x],user_id[y]) and check[y]==0:
                check[y]=0
                ans.append(user_id[y])
    for x in ans:
        print(x)
    
    comb=list(combinations(ans,len(banned_id)))
    answer=len(comb)
    return answer
comb=list(combinations(nlist,n//2))
for x in comb:
    check=[False for _ in range(n)]
    for y in x:
        check[y]=True
    solve(x,check)

print(ans)
