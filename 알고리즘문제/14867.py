fa,fb,sa,sb = map(int,input().split())
MAX=-1
temp=[0,0,0]
af=[MAX for x in range(100000) for y in range(4)]
ae=af[0:]
bf=af[0:]
be=af[0:]
bfs=[]

def mypush(a,b,d):
    if a==0:
        if ae[b]==MAX:
            ae[b]=d
            bfs.append([a,b,d])
            return
    elif a==fa:
        if af[b] == MAX:
            af[b]=d
            bfs.append([a,b,d])
            return
    elif b==0:
        if be[a] == MAX:
            be[a]=d
            bfs.append([a,b,d])
            return
    elif b==fb:
        if bf[a]==MAX:
            bf[a]=d
            bfs.append([a,b,d])
            return
            
def dis(sa,sb):
    if sa==0:
        return ae[sb]
    if sa==fa:
        return af[sb]
    if sb==0:
        return be[sa]
    if sb==fb:
        return bf[sa]
    else:
        return -1
mypush(0,0,0)
while bfs:
    temp=bfs.pop(0)
    wa=temp[0]
    wb=temp[1]
    d=temp[2]
    mypush(wa,0,d+1)
    mypush(wa,fb,d+1)
    mypush(0,wb,d+1)
    mypush(fa,wb,d+1)
    tmp=min(wa,fb-wb)
    mypush(wa-tmp,wb+tmp,d+1)
    tmp=min(fa-wa,wb)
    mypush(wa+tmp,wb-tmp,d+1)
    

if dis(sa,sb)==MAX:
    print("-1")
else:
    print(dis(sa,sb))
    
    
