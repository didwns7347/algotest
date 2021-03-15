w,h=map(int,input().split())
box=[]
cnt=1
q=[]
s=[[1,0],[0,1],[-1,0],[0,-1]]
for x in range(h):
    tmp=list(map(int, input().split()))
    box.append(tmp)
for x in box:
    print(x)
check=[[0]*w]*h

for x in range(h):
    for y in range(w):
        if box[x][y]==1 and check[x][y]==0:
            t=[]
            t.append(x)
            t.append(y)
            q.append(t)
            check[x][y]=1
            while(True):
                print(q)
                if not q:
                    break
                tmp=q.pop()
                for x in s:
                    nx,ny=tmp[0]+x[0],tmp[1]+x[1]
                    
                    if nx>=h or nx<0 or ny>=w or ny<0:
                        continue
                    print(nx,ny)
                    if box[nx][ny]==0 and check[nx][ny]==0:
                        t=[]
                        t.append(nx)
                        t.append(ny)
                        q.append(t)
                        check[nx][ny]=1
                        box[nx][ny]=box[tmp[0]][tmp[1]]+1
                        
                print(t)
            

for x in box:
    print("box=",x)

for x in check:
    print("xheck=",x)
