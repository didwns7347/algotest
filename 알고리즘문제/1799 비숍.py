n=int(input())
bzone=[]
wzone=[]
board=[]
wans=0
bans=0
for i in range(n):
    board.append(list(map(int,input().split())))
    

for x in range(n):
    for y in range(n):
        if board[x][y]==1 and x%2==0 :
            if y%2==0:
                bzone.append([x,y])
            else:
                wzone.append([x,y])
        elif board[x][y]==1 and x%2==1 :
            if y%2==0:
                wzone.append([x,y])
            else:
                bzone.append([x,y])
        



def BBF(i,cnt,bd,ck1,ck2):
    if i==len(bzone):
        global bans
        bans=max(bans, cnt)
        return
    #print(zone[i][0],zone[i][1])
    a=bzone[i][0]
    b=bzone[i][1]
    if ck1[b-a+n-1]==0 and ck2[a+b]==0:
        ck1[b-a+n-1]=1
        ck2[b+a]=1
        bd[a][b]=2
        BBF(i+1,cnt+1,bd,ck1,ck2)
        ck1[b-a+n-1]=0
        ck2[b+a]=0
        bd[a][b]=0
        BBF(i+1,cnt,bd,ck1,ck2)
    else:
        BBF(i+1,cnt,bd,ck1,ck2)

def BF(i,cnt,bd,ck1,ck2):
    if i==len(wzone):
        global wans
        wans=max(wans, cnt)
        return
    #print(zone[i][0],zone[i][1])
    a=wzone[i][0]
    b=wzone[i][1]
    if ck1[b-a+n-1]==0 and ck2[a+b]==0:
        ck1[b-a+n-1]=1
        ck2[b+a]=1
        bd[wzone[i][0]][wzone[i][1]]=2
        BF(i+1,cnt+1,bd,ck1,ck2)
        ck1[b-a+n-1]=0
        ck2[b+a]=0
        bd[wzone[i][0]][wzone[i][1]]=0
        BF(i+1,cnt,bd,ck1,ck2)
    else:
        BF(i+1,cnt,bd,ck1,ck2)

        
            
BF(0,0,board,[0]*(n*2-1),[0]*(n*2-1))
BBF(0,0,board,[0]*(n*2-1),[0]*(n*2-1))
print(wans+bans)
