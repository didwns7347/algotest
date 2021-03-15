import collections
import sys
st=sys.stdin.readline().strip()

n=int(sys.stdin.readline())
lst=collections.deque(st)
rst=collections.deque()

for x in range(n): 
    op=sys.stdin.readline().strip()
    if op[0]=="L" and lst:
        rst.appendleft(lst.pop())
    if op[0]=='D' and rst:
        lst.append(rst.popleft())
    if op[0]=="B" and lst:
        lst.pop()      
    if op[0]=="P" :
        lst.append(op[2])


sys.stdout.write(''.join(lst) + ''.join(rst))
