s="{{4,2,3},{3},{2,3,4,1},{2,3}}"
s=s[1:-1]
t=[]
for x in s:
    if x=="{":
        tmp=''
    elif x=="}":
        t.append(list(map(int,tmp.split(","))))
    else:
        tmp+=x
t.sort(key=len)
for x in t:
    print(x)
    

tmp=''
def solution(s):
    check=[0 for x in range(100000)]
    s=list(s)
    answer = []
    tmp=''
    for x in s:
        if x not in ["{","}"]:
            tmp+=x
    print(tmp)
    st=list(map(int,tmp.split(",")))
    for x in st:
        if check[x]==0:
            answer.append(x)
            check[x]=1
    
    return answer
