h,w=map(int,input())
ans=0
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

dx=[1,0,-1,0]
dy=[0,1,0,-1]
def move(rx,ry,bx,by,d,n):
        Rfin=False
        Bfin=False
        if n>10:
            ans=11
            return
        rnx=rx
        rny=ry
        bnx=bnx
        bny=bny
        while True:
            if m[rnx+dx[d]][rny+dy[d]]=="#":
                break
            if m[rnx+dx[d]][rny+dy[d]]=="O":
                Rfin=True
            
            rnx+=dx[d]
            rny+=dy[d]

        while True:
            if m[bnx+dx[d]][bny+dy[d]]=="#":
                break
            if m[bnx+dx[d]][bny+dy[d]]=="O":
                Bfin=True
            bnx+=dx[d]
            bny+=dy[d]
        if Bfin ==True:
            return
        else:
            if Rfin==True
                ans=min(ans,n)
                return
        
