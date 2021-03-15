import sys
n,m=map(int,input().split())
namedict={}
out=[]
for x in range(n):
    name=sys.stdin.readline().strip()
    namedict[name]=1

for x in range(m):
    name=sys.stdin.readline().strip()
    if name in namedict:
        out.append(name)

print(len(out))

for x in out:
    print(x)
