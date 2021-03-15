from sys import stdin
input = stdin.readline
n=int(input())
import  sys
sys.setrecursionlimit(100000)
depth=[0 for _ in range(n+1)]
parent=[x for x in range(n+1)]
g=[[] for _ in range(n+1)]
def dfs(start, d):
    depth[start]=d
    for nxt in g[start]:
        dfs(nxt,d+1)
        parent[nxt]=start
def find(a,ad,b,bd):
    if ad>bd:
        while ad != bd:
            ad-=1
            a=parent[a]
    elif ad<bd:
        while bd!=ad:
            bd-=1
            b=parent[b]
    
    while a!=b:
        a=parent[a]
        b=parent[b]
            
    return a
        
    
for _ in range(n-1):
    a,b=map(int,input().split())
    if a>b:
        g[b].append(a)
    else:
        g[a].append(b)

dfs(1,1)

m=int(input())
for _ in range(m):
    a,b=map(int,input().split())
    print(find(a,depth[a],b,depth[b]))
    
