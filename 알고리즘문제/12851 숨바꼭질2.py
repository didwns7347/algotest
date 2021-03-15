from collections import deque
n,tg=map(int,input().split())
dist=[-1 for x in range(100001)]

q=deque()
q.append(n)
dist[n]=0

answer=0
while q:
    x=q.popleft()
    if x==tg:
        answer+=1

    if x-1>=0 :
        if dist[x-1]==-1 or dist[x-1]==dist[x]+1:
            dist[x-1]=dist[x]+1
            q.append(x-1)
        
    if x+1<=100000:
        if dist[x+1]==-1 or dist[x+1]==dist[x]+1:
            dist[x+1]=dist[x]+1
            q.append(x+1)
        
    if x*2<=100000:
        if dist[x*2]==-1 or dist[2*x]==dist[x]+1:
            dist[x*2]=dist[x]+1
            q.append(x*2)
      
    


print(dist[tg])     
print(answer)
