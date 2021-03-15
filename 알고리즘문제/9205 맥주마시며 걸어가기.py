from collections import deque
import sys
for _ in range(int(input())):
    n=int(sys.stdin.readline())
    hx,hy=map(int,sys.stdin.readline().split())
    point=[[0,0]]
    for _ in range(n):
        x,y=map(int ,sys.stdin.readline().split())
        point.append([x-hx,y-hy])
    fx,fy=map(int,sys.stdin.readline().split())
    point.append([fx-hx,fy-hy])
    
    board=[[0 for x in range(n+2)] for y in range(n+2)]
    check=[0 for x in range(n+2)]
    for x in range(n+2):
        for y in range(n+2):
            if x==y:
                continue
            board[x][y]=abs(point[x][0]-point[y][0])+abs(point[x][1]-point[y][1])
    
    q=deque()
    q.append(0)
    answer="sad"
    while True:
        if not q:
            break
        x=q.popleft()
        if x==n+1:
            answer="happy"
            break
        check[x]=1
        for i in range(n+2):
            if i==x:
                continue
            else:
                if board[x][i]<=1000 and check[i]==0:
                    q.append(i)
                    
    print(answer)


        
