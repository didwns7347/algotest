R,C=map(int,input().split())
ans=1
m=[]
check=[ 0 for x in range(26)]
cposi=[[0 for x in range(C)] for y in range(R)]
for x in range(R):
    tmp=list(input())
    m.append(tmp)


ans=0
def do(x,y,n):
    global ans
    ans=max(ans,n)
    if n==R*C:
        return 0
    if x<R-1 and cposi[x+1][y]==0 and check[ord(m[x+1][y])-65]==0:
        cposi[x+1][y]=1
        check[ord(m[x+1][y])-65]=1
        do(x+1,y,n+1)

        cposi[x+1][y]=0
        check[ord(m[x+1][y])-65]=0
    if y<C-1 and cposi[x][y+1]==0 and check[ord(m[x][y+1])-65]==0:
        cposi[x][y+1]=1
        check[ord(m[x][y+1])-65]=1
        do(x,y+1,n+1)

        cposi[x][y+1]=0
        check[ord(m[x][y+1])-65]=0

    if x>0 and cposi[x-1][y]==0 and check[ord(m[x-1][y])-65]==0:
        cposi[x-1][y]=1
        check[ord(m[x-1][y])-65]=1
        do(x-1,y,n+1)
     
        cposi[x-1][y]=0
        check[ord(m[x-1][y])-65]=0
    if y>0 and cposi[x][y-1]==0 and check[ord(m[x][y-1])-65]==0:
        cposi[x][y-1]=1
        check[ord(m[x][y-1])-65]=1
        do(x,y-1,n+1)
        
        cposi[x][y-1]=0
        check[ord(m[x][y-1])-65]=0
    return 0
check[ord(m[0][0])-65]=1
cposi[0][0]=1
do(0,0,1)
print(ans)

