m=[]
out=[]
def push(x):
    m.append(x)

def pop():
    if len(m)==0:
        out.append(-1)
    else:
        out.append(m.pop(0))
def front():
    if m:
        out.append(m[0])
    else:
        out.append(-1)
def back():
    if m:
        out.append(m[-1])
    else:
        out.append(-1)

def size():
    out.append(len(m))

def empty():
    if m:
        out.append(0)
    else:
        out.append(1)


n = int(input(""))
op=[]
for i in range(n):
    op = input().split()
    if op[0] == "push":
        push(int(op[1]))
    elif op[0] == "pop":
        pop()
    elif op[0] == "size":
        size()
    elif op[0] == "empty":
        empty()
    elif op[0] == "front":
        front()
    elif op[0] == "back":
        back()
for x in out:
    print(x)
