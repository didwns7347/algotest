n,l = map(int,input().split())

wboard=[]
for x in range(n):
    wboard.append(list(map(int,input().split())))
hboard=[]
for x in range(n):
    tmp=[]
    for y in range(n):
        tmp.append(wboard[y][x])
    hboard.append(tmp) 
def simul(arr):
    sta=[0 for x in range(n)]
    d=1
    for x in range(n-1):

        if arr[x]==arr[x+1] :
            if sta[x]==0:
                d+=1
        else:
            if arr[x+1]-1==arr[x]:
                if d>=l:
                    for x in range(x+1-d,x+1):
                        if sta[x]==1:
                            return False
                    d=1
                    continue
                else:
                    return False
            elif arr[x+1]+1==arr[x]:
                if x+l>=n:
                    return False
                tmp=arr[x+1]
                ctmp=True
                for i in range(x+1,x+1+l):
                    if tmp != arr[i] or sta[i]!=0:
                        ctmp=False
                        return False
                if ctmp:
                    for i in range(x+1,x+1+l):
                        sta[i]=1
            else:
                return False
            d=1
    #print(arr,sta)
    return True

def check(board):
    out=0
    for tmp in board:
        if simul(tmp):
            #print(tmp)
            out+=1
    return out
answer=check(wboard)+check(hboard)
print(answer)
