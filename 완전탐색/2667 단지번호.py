import sys

sys.setrecursionlimit(2000)
n=int(input())
m=[]
for x in range(n):
    t=sys.stdin.readline()
    tmp=[]
    for s in t:
        tmp.append(int(s))
    m.append(tmp)
        
for x in m:
    print(x)

