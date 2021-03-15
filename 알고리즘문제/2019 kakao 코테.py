import itertools
from itertools import combinations
def solution(user_id, banned_id):
    answer=0

    comb=list(combinations(user_id,len(banned_id)))
  
    for x in comb:
        
        if compare(x,banned_id):
            answer+=1
            
    

    return answer

def compare(a,b):
    m=list(itertools.permutations(a))

    cnt=0
    while True:
        if cnt==len(m):
            break
        a=m[cnt]
        eq=0
        check=[0 for x in range(len(b))]
        for x in range(len(a)):
            for y in range(len(b)):
                if comp(a[x],b[y]) and check[y]==0:
                    check[y]+=1
                    eq+=1
                    break
        if eq==len(b):
            return True
        cnt+=1
    return False
def comp(user,ban):
    ecnt=0
    if len(ban)==len(user):
        for i in range(len(ban)):
            if ban[i]==user[i] or ban[i]=="*":
                ecnt+=1

    if ecnt==len(user):
        return True
   
    return False

a=["frodo", "fradi", "crodo", "abc123", "frodoc"]
b=["fr*d*", "*rodo", "******", "******"]
print(solution(a,b))
