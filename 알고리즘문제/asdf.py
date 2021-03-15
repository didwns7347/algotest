def solution(expression):
    answer=0
    op=[["+","-","*"],["+","*","-"],["-","*","+"],["-","+","*"],["*","-","+"],["*","+","-"]]
    n=''
    tmp=[]
    for x in range(len(expression)):
        if expression[x] in ["+","-","*"]:
            tmp.append(int(n))
            tmp.append(expression[x])
            n=''
        else:
            n+=expression[x]
        if x==len(expression)-1:
            tmp.append(int(n))
    for x in range(6):
        a=tmp
        for y in range(3):
            a=calc(a,op[x][y])
        answer=max(abs(a[0]),answer)
      
    return answer
def calc(t,op):
    re=[]
    p=len(t)
    for x in range(len(t)):
        if x==p:
            continue
        if t[x]==op and op=="+":
            re[-1]=re[-1]+t[x+1]
            p=x+1
        elif t[x]==op and op=="-":
            re[-1]=re[-1]-t[x+1]
            p=x+1
        elif t[x]==op and op=="*":
            re[-1]=re[-1]*t[x+1]
            p=x+1
        else:
            re.append(t[x])
    return re
            
print(solution("100-200*300-500+20"))
