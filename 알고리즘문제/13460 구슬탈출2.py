h,w=map(int,input().split())
ans=11
m=[list(input()) for _ in range(h)]
for x in range(h):
    for y in range(w):
        if m[x][y]=="B":
            Bx=x
            By=y
        if m[x][y]=="R":
            Rx=x
            Ry=y
        if m[x][y]=="O":
            Ox=x
            Oy=y
#0북 1 동  2남 3서
            
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def skeep(x):
    if x==0:
        return 1
    elif x==1:
        return 0
    elif x==2:
        return 3
    elif x==3:
        return 2
def move(rx,ry,bx,by,d,n):
        global ans
        Rfin=False
        Bfin=False
        

        
        if n>10:
            return
        rnx=rx
        rny=ry
        bnx=bx
        bny=by
        while True:

            if m[rnx+dx[d]][rny+dy[d]]=="#":
                break
            if m[rnx+dx[d]][rny+dy[d]]=="O":
                Rfin=True
                break
            
            rnx+=dx[d]
            rny+=dy[d]

        while True:

            if m[bnx+dx[d]][bny+dy[d]]=="#":
                break
            if m[bnx+dx[d]][bny+dy[d]]=="O":
                Bfin=True
                break
            bnx+=dx[d]
            bny+=dy[d]
        if Bfin ==True:
            return
        else:
            if Rfin==True:
                ans=min(ans,n)
                return
        if rnx==bnx and rny==bny:
            if abs(rx-rnx)+abs(ry-rny)< abs(bx-bnx)+abs(by-bny):
                  bnx=bnx-dx[d]
                  bny=bny-dy[d]
            else:
                  rnx=rnx-dx[d]
                  rny=rny-dy[d]
        for x in range(4):
            if x==d or x==skeep(x):
                  continue
            move(rnx,rny,bnx,bny,x,n+1)

move(Rx,Ry,Bx,By,0,1)
move(Rx,Ry,Bx,By,1,1)
move(Rx,Ry,Bx,By,2,1)
move(Rx,Ry,Bx,By,3,1) 
if ans>10:
      ans=-1
print(ans)
         
        
