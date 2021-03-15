import sys
a,b,c=map(int,input().split())
dead=[0 for _ in range(c)]
d=[[0,0],[-1,0],[1,0],[0,1],[0,-1]]
t=["a","b","c","d","e","f","g","h"]
aa=[0]
if c==0:
    print(0)
    sys.exit()
tmp=1
ck=False
for x in range(2003):
    if ck:
        aa.append(tmp)
        tmp-=1
        if tmp==1:
            ck=False
    else:
        aa.append(tmp)
        tmp+=1
        if tmp==a:
            ck=True
bb=[0]
ck=False
tmp=1
for x in range(2003):
    if ck:
        bb.append(tmp)
        tmp-=1
        if tmp==1:
            ck=False
    else:
        bb.append(tmp)
        tmp+=1
        if tmp==b:
            ck=True
#print(aa[0:200])
#print(bb[0:200])
         
data=[]
for x in range(c):
    data.append(list(map(int ,input().split())))


def move():
    delete=[]
    check=[ [-1 for _ in range(b+1)] for _ in range(a+1)]
   
    for i in range(c):
        if dead[i]:
            continue
        
        if data[i][3]==1:
            for x in range(a,a+a+2):
                if aa[x]==data[i][0]:
                    start=x
                    break
            
            if aa[start+data[i][2]+1]>aa[start+data[i][2]]:
                data[i][3]=2
            data[i][0]=aa[start+data[i][2]]
                
        elif data[i][3]==2:
            for x in range(1,a+1):
                if aa[x]==data[i][0]:
                    start=x
                    break
            if aa[start+data[i][2]+1]<aa[start+data[i][2]]:
                data[i][3]=1
            
            data[i][0]=aa[start+data[i][2]]

        elif data[i][3]==3:
            for x in range(1,b+1):
                if bb[x]==data[i][1]:
                    start=x
                    break
            if bb[start+data[i][2]+1]<bb[start+data[i][2]]:
                data[i][3]=4
            data[i][1]=bb[start+data[i][2]]
            
        elif data[i][3]==4:
            for x in range(b,b+b):
                if bb[x]==data[i][1]:
                    start=x
                    break
            if bb[start+data[i][2]+1]>bb[start+data[i][2]]:
                data[i][3]=3
            
            data[i][1]=bb[start+data[i][2]]
          
           
        if check[data[i][0]][data[i][1]]!=-1:
            tmp=check[data[i][0]][data[i][1]]
            if data[tmp][4]>data[i][4]:
                delete.append(i)
            else:
                delete.append(tmp)
                check[data[i][0]][data[i][1]]=i
        else:
            check[data[i][0]][data[i][1]]=i
    for x in delete:
        dead[x]=1

            
out=[]
ans=0
catch=1

for x in range(1,b+2):
    tmp=float("inf")
    eat=-1

    for y in range(c):
        if dead[y]:
            continue
        if data[y][1]==x :
            if data[y][0]<tmp:
                tmp=data[y][0]
                eat=y
    if eat>=0 :
        ans+=data[eat][4]
        dead[eat]=1
    move()
                
            
       
print(ans)
