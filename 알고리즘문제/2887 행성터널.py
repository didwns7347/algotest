from sys import stdin
input = stdin.readline
n=int(input())
space=[]
univer=[]
cost=0
for i in range(n):
    a,b,c=map(int,input().split())
    space.append([a,b,c,i])

for  i in range(3):
    space.sort(key=lambda x:x[i])
    now=space[0][3]
    for j in range(1,n):
        nxt=space[j][3]
        univer.append([abs(space[j][i]-space[j-1][i]),now,nxt])
        now=nxt
        
        


univer.sort(key=lambda x:x[0])

parent=[ x for x in range(n)]
def union(a,b):
    ta=find(a)
    tb=find(b)
    if ta==tb:
        return False
    elif ta<tb:
        parent[tb]=ta
    else:
        parent[ta]=tb
    return True
def find(a):
    if a==parent[a]:
        return a
    tmp=find(parent[a])
    parent[a]=tmp
    return tmp
cnt=0
for c,a,b in univer:
    if union(a,b):
        cost+=c
        cnt+=1
    if cnt==n-1:
        print(cost)
        break













        
