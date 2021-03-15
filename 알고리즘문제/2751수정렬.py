import sys
n=int(input())
a=[]
for x in range(n):
    t=sys.stdin.readline().strip()
    if not t:
        break
    t=int(t)
    a.append(t)

a.sort()
for x in a:
    print(x)
