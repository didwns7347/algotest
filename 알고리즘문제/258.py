m=[list(map(int,input().split())) for x in range(9)]
q=[]
cr=[[0 for x in range(10)] for y in range(10)]
cc=[[0 for x in range(10)] for y in range(10)]
cj=[[0 for x in range(10)] for y in range(10)]
f=False
for x in range(9):
    for y in range(9):
        if m[x][y]==0:
            q.append([x,y])
        else:
            cr[x][m[x][y]]=1
            cc[y][m[x][y]]=1
            cj[x//3*3+y//3][m[x][y]]=1
def do(x,y,l):
    global f
    if l>=len(q):
        return True
    for i in range(1,10):
        if cr[x][i]==0 and cc[y][i]==0 and cj[x//3*3+y//3][i]==0:
            cr[x][i]=1
            cc[y][i]=1
            cj[x//3*3+y//3][i]=1
            m[x][y]=i
            if l+1 == len(q):
                f=True
                return True
            do(q[l+1][0],q[l+1][1],l+1)
            if f==True:
                return True
            m[x][y]=0
            cr[x][i]=0
            cc[y][i]=0
            cj[x//3*3+y//3][i]=0
    return False

            
        
        
if do(q[0][0],q[0][1],0):
    for x in m:
        for y in x:
            print(y,end=' ')
        print()

else:
    print(-1)
