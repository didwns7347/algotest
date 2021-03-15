def solution(s):
    answer = len(s)
    s=list(s)
    f=len(s)//2
    
    for x in range(1,f+1):
        #answer=min(answer,zip(s,x))
        print(x,zip(s,x))
    return answer
def zip(s,n):
    tmp=[]
    cnt=0
    st=[]
    for x in range(len(s)):
        tmp.append(s[x])
        if len(tmp)==n or x==len(s)-1:
            st.append(tmp)
            tmp=[]
    stack=[]      
    for x in st:
        if not stack or stack[-1]!=x:
            stack.append(0)
            stack.append(x)
        if stack[-1]==x:
            tmp=stack.pop()
            stack[-1]+=1
            stack.append(tmp)
    print(st)
    out=''
    for x in stack:
        if x ==1:
            continue
        if type(x)==list:
            out+="".join(x)
        else:
            out+=str(x)
    
    return out

s="aabbaccc"
print(solution(s))
