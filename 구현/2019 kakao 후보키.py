from itertools import combinations
def solution(relation):
    answer=[]
    n=len(relation[0])
    superkey=[]
    a=[x for  x in range(len(relation[0]))]
    for x in range(1,n+1):
        superkey+=list(combinations(a,x))

    for y in superkey:
        if check(relation,y):
            answer.append(y)
    
    for x in range(0,len(answer)-1):
        for y in range(x+1,len(answer)):
            if answer[x] and answer[y] and ch(answer[x],answer[y]):
                answer[y]=[]
    acnt=0
    for x in answer:
        if x:
            acnt+=1
           
    return acnt
def check(r,sup):
    clist=[]
    for x in r:
        tmp=''
        for y in sup:
            tmp+=x[y]
        if tmp in clist:
            return False
        clist.append(tmp)
    return True
def ch(a,b):
    cnt=0
    for x in a:
        for y in b:
            if x==y:
                cnt+=1
    if cnt==len(a):
        return True
    return False
        
print(solution([["100","ryan","music","2"],["200","apeach","math","2"],
                ["300","tube","computer","3"],["400","con","computer","4"],
                ["500","muzi","music","3"],["600","apeach","music","2"]]))
