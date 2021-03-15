import sys

sys.setrecursionlimit(100000)
n,r1,r2=map(int,input().split())
cave=[[] for x in range(n+1)]
check=[0 for x in range(n+1)]

line=[]
def dfs(n):
    global line
    check[n]=1
    for x in cave[n]:
        if check[x[0]]!=1:
            line.append([x[0],x[1]])
            if x[0]==r2:
                break 
            dfs(x[0])
    if line[-1][0]!=r2 and len(line)!=0:
        line.pop()
for x in range(n-1):
    a,b,d=map(int,sys.stdin.readline().split())
    cave[a].append([b,d])
    cave[b].append([a,d])

m=0
s=0


dfs(r1)

for x in range(len(line)):
    s=s+line[x][1]
    m=max(m,line[x][1])
print(s-m)




