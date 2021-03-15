import sys
n=int(input())
p=list(map(int , sys.stdin.readline().split()))

p.sort()
out=[0 for x in range(n)]

for x in range(len(p)):
    out[x]=sum(p[0:x+1])

print(sum(out))
