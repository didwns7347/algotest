import sys

n=int(sys.stdin.readline())

w=[]

INF =sys.maxsize

for _ in range(n):
    w.append(list(map(int,input().split())))
dp=[[None]*(1<<n) for _ in range(n)]
for x in dp:
    print(x)
def find(last,visited):
    print(visited)
    if visited == (1<<n)-1:
        return w[last][0] or INF

    if dp[last][visited] is not None:
        return dp[last][visited]
    tmp=INF
    for city in range(n):
        if visited & (1<<city)== 0 and w[last][city]!=0:
            tmp=min(tmp, find(city,visited| (1<<city)) + w[last][city])
    dp[last][visited]=tmp
    return tmp
for x in dp:
    print(x)
print(find(0,1<<0))
