n=int(input())
p="I"
for x in range(n):
    p+="OI"
m=int(input())
st=list(input())
p=list(p)
answer=0
stack=[]
answer=[]
for x in range(len(st)):
    if st[x]=="I" and not stack:
        stack.append(st[x])
        continue
    if st[x]=="O" and not stack:
        continue
    if stack[-1]=="I" and st[x]=="O":
        stack.append(st[x])
    elif stack[-1]=="O" and st[x]=="I":
        stack.append(st[x])
    else :
        if stack[-1]=="O":
            stack.pop()
            answer.append(len(stack))
            stack=[]
        else:
            answer.append(len(stack))
            stack=["I"]
if len(stack)>2:
    answer.append(len(stack))
out=0
for x in answer:
    if x<len(p):
        continue
    out=(x-len(p))//2+1+out

print(out)
