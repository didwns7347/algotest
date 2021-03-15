from itertools import combinations
n,m=map(int,input().split())
city=[list(map(int,input().split())) for _ in range(n)]
bbq=[]
house=[]
for x in range(n):
    for y in range(n):
        if city[x][y]==2:
            bbq.append([x,y])
        if city[x][y]==1:
            house.append([x,y])
lbbq=list(combinations(bbq,m))

answer=n*n*m*n
for x in lbbq:
    ckdist=0
    for y in house:
        tmp=n+n
        for z in x:
            dist=abs(y[0]-z[0])+abs(y[1]-z[1])
            tmp=min(tmp,dist)
            #print(y,z,dist)
        ckdist+=tmp
    #print(ckdist)
    answer=min(answer,ckdist)
print(answer)