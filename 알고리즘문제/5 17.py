from collections import deque
n, m = map(int,input().split())
dist=[0 for _ in range(100001)]
check=[0 for _ in range(100001)]
q=deque()
q.append(n)
check[n]=1

while q:
    tmp=q.popleft()
    if tmp==m:
        print(dist[tmp])
        break
    if tmp*2<=100000 and check[tmp*2]==0 :
        check[tmp*2]=1
        dist[tmp*2]=dist[tmp]
        q.append(tmp*2)
        
    if tmp-1>=0 and check[tmp-1]==0 :
        check[tmp-1]=1
        dist[tmp-1]=dist[tmp]+1
        q.append(tmp-1)
    if tmp+1<=100000 and check[tmp+1]==0 :
        check[tmp+1]=1
        dist[tmp+1]=dist[tmp]+1
        q.append(tmp+1)
    
