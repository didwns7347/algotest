import sys
import collections
n = int(input())

out=[]

def func(op,ar):
    for x in range(len(op)):
        if op[x]=="R":
            ar.reverse()
        elif op[x]=="D":
            if ar:
                ar.popleft()
            else:
                out.append('error')
                return
    out.append(ar)
    return
                   
for x in range(n):
    for y in range(3):
        if y==0:
            op=list(sys.stdin.readline().strip())
            if len(op)>=2:
                for x in range(len(op)-1):
                    if op[x]=='R' and op[x+1]=='R':
                        op[x],op[x+1]='',''
        elif y==1:
            num=int(sys.stdin.readline().strip())
        else:
            st=sys.stdin.readline().strip()
            st=st[1:len(st)-1]
            if st:
                ar=collections.deque(st.split(','))
            else:
                ar=collections.deque()
 
    func(op,ar)

for x in out:
    if type(x)==str:
        print(x)
    else:
        print(list(x))

