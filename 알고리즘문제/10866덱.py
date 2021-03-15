import collections
deq=collections.deque()
n=int(input())
out=[]
for x in range(n):
    op=input().split()
    if op[0]=="push_front":
        deq.appendleft(op[1])

    elif op[0]=="push_back":
        deq.append(op[1])

    elif op[0]=="pop_front":
        if deq:
            out.append(deq.popleft())
        else:
            out.append(-1)

    elif op[0]=="pop_back":
        if deq:
            out.append(deq.pop())
        else:
            out.append(-1)

    elif op[0]=="size":
        out.append(len(deq))

    elif op[0]=="empty":
        if deq:
            out.append(0)
        else:
            out.append(1)

    elif op[0]=="front":
        if deq:
            out.append(deq[0])
        else:
            out.append(-1)
        
    else :
        if deq:
            out.append(deq[-1])
        else:
            out.append(-1)

for x in out:
    print(x)
        
        
