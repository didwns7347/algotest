def solution(p):
    if p=='':
        return ""
    if check(p)==True:
        return p
    u,v=div(p)
    if check(u):
        return u+solution(v)
    else:
        tmp="("  
        a=solution(v)
        tmp=tmp+a+")"
        tmp+=go(u)
        return tmp
    answer = ''
    return answer
def check(s):
    tmp=[]
    for x in s:
        if x=="(":
            tmp.append("(")
        else:
            if not tmp:
                return False
            tmp.pop()
    return True
def div(s):
    left=[]
    right=[]
    for x in range(len(s)):
        if s[x]=="(":
            left.append(1)
        else:
            right.append(1)
        if x%2==1 and len(left)==len(right) :
            a=s[0:x+1]
            b=s[x+1:]
            break
    return a,b
def go(u):
    out=''
    if len(u)<3:
        return ""
    for x in range(1,len(u)-1):
        if u[x]=="(":
            out+=")"
        else:
            out+="("
    return out
        

print(solution("()))((()"))
