sx=[-1, -1, -1, 0, 1, 1, 1, 0]
sy=[-1, 0, 1, 1, 1, 0, -1, -1]
w=0
h=0
def dfs(a,b):
    check[a][b]=1
    for x in range(8):
        na,nb=a+sx[x],b+sy[x]        
        if na<0 or na>=h or nb<0 or nb>=w:
            continue

        if m[na][nb] and check[na][nb]==0 :
            dfs(na,nb)
    

while True:
    w,h= map(int,input().split())
    cnt=0
    if w==0 and h==0:
        break
    m=[]
    for x in range(h):
        tmp=list(map(int,input().split()))
        m.append(tmp)

    check=[[0 for x in range(w)] for y in range(h)]


    for x in range(h):
        for y in range(w):
            if check[x][y]==0 and m[x][y]:
                dfs(x,y)
                cnt+=1
    print(cnt)


