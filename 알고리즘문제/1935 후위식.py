import sys
n=int(sys.stdin.readline().strip())
ex=sys.stdin.readline().strip()
ex=list(ex)
num=[]
st=[]

for x in range(n):
    num.append(int(sys.stdin.readline().strip()))
    
for x in range(len(ex)):
    if ex[x]=="*":
        st.append(st.pop()*st.pop())
    elif ex[x]=="+":
        st.append(st.pop()+st.pop())
    elif ex[x]=="/":
        a=st.pop()
        b=st.pop()
        st.append(b/a)
    elif ex[x]=="-":
        a=st.pop()
        b=st.pop()
        st.append(b-a)
    else:
        st.append(num[ord(ex[x])-65])

print(format(st[0],".2f"))
        
