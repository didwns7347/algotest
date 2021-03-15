#N=0 S=1
from collections import deque
gears=[]
d=[0,0,0,0]

def rotation(check,idx,c):
    if check[idx]==0:
        check[idx]=c
    else:
        return
    if idx-1>=0 and gears[idx-1][2]!=gears[idx][6]:
        rotation(check,idx-1,c*-1)
    elif idx-1>=0 and gears[idx-1][2]==gears[idx][6]:
        check[idx-1]=2
        
    if idx+1<4 and gears[idx+1][6]!=gears[idx][2]:
        rotation(check,idx+1,c*-1)
    elif idx+1<4 and gears[idx+1][6]==gears[idx][2]:
        check[idx+1]=2
for x in range(4):
    q=deque()
    tmp=list(input())
    for x in tmp:
        q.append(int(x))
    gears.append(q)
n=int(input())
answer=0

for x in range(n):
    idx,course=map(int,input().split())
    check=[0,0,0,0]
    rotation(check,idx-1,course)
    for x in range(4):
        if check[x]==0 or check[x]==2:
            continue
        if check[x]==1:
            gears[x].appendleft(gears[x].pop())
        if check[x]==-1:
            gears[x].append(gears[x].popleft())
answer=0
for x in range(4):
    if gears[x][0]==1:
        answer=answer+2**x
print(answer)
    
   
