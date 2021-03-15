def solution(user_id, banned_id):
    check=[x for x in range(len(user_id))]
    answer = 1
    cnt=0
    t=[0 for x in range(len(banned_id))]
    
    for x in range(len(banned_id)):
        for y in range(len(user_id)):
            if comp(banned_id[x],user_id[y]) and check[y]==0:
                check[y]=1
                t[cnt]+=1
        cnt+=1
    for x in t:
        answer*=x
    return answer
def comp(ban,user):
    ecnt=0
    if len(ban)==len(user):
        for i in range(len(ban)):
            if ban[i]==user[i] or ban[i]=="*":
                ecnt+=1
    if ecnt==len(user):
        return True
    return False
            
