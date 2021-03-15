from collections import deque
import copy
h,w=map(int,input().split())
ans=0
m=[]
q=deque()
dx=[1,-1,0,0]
dy=[0,0,-1,1]
tcnt=0
ocnt=0
for x in range(h):
    m.append(list(map(int,input().split())))

for x in range(h):
    for y in range(w):
        if m[x][y]==2:
            tcnt+=1
            q.append([x,y])
        if m[x][y]==1:
            ocnt+=1
def gob(a,b,c,q,m):
    cnt=tcnt
    board=copy.deepcopy(m)
    board[a[0]][a[1]]=1
    board[b[0]][b[1]]=1
    board[c[0]][c[1]]=1

    queue=copy.deepcopy(q)
    
    while queue:
        tx,ty=queue.popleft()
        
        for i in range(4):
            tmx=tx+dx[i]
            tmy=ty+dy[i]
            
            if tmx>=0 and  tmx<h and  tmy>=0 and tmy<w:
                if board[tmx][tmy]==0:
                    queue.append([tmx,tmy])
                    board[tmx][tmy]=2
                    cnt+=1
    

    return w*h-cnt-ocnt-3
                

for x in range(h*w):
    if m[x//w][x%w]==0:
        xx=x//w
        xy=x%w
    for y in range(h*w):
        if x==y:
            continue
        if m[y//w][y%w]==0 and m[x//w][x%w]==0:
            yx=y//w
            yy=y%w
        for z in range(h*w):
            if x==z or y==z:
                continue
            if m[z//w][z%w]==0 and m[x//w][x%w]==0 and m[y//w][y%w]==0 :
                zx=z//w
                zy=z%w
                ans=max(gob([xx,xy],[yx,yy],[zx,zy],q,m),ans)
               
           
print(ans)
