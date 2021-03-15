import bisect
n,m,k = map(int,input().split())
card=list(map(int,input().split()))
card.sort()

ubound=[x for x in range(m)]
draw=list(map(int,input().split()))
def find(num):
    if ubound[num]==num:
        ubound[num]=num+1
        return num+1
    tmp=find(ubound[num])
    ubound[num]=tmp
    return tmp
for num in draw:
    idx=bisect.bisect(card,num)
    out=find(idx)
    print(card[out-1])
    

