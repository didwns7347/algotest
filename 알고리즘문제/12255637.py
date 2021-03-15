m=[]
out=[]
def push(x):
    m.append(x)

def pop():
    if len(m)==0:
        out.append(-1)
    else:
        out.append(m.pop())

def size():
    out.append(len(m))

def empty():
    if m:
        out.append(0)
    else:
        out.append(1)

def top():
    if len(m)==0:
        out.append(-1)
    else:
        out.append(m[len(m)-1])

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
    elif op[0] == "top":
        top()

for x in out:
    print(x)
