n=int(input())
nums=list(map(int,input().split()))

#+-x/
op=list(map(int,input().split()))
maxans=-1000000001
minans=1000000001
def do(num,i,a,b,c,d):

    global maxans,minans
    if i==n:
        maxans=max(maxans,num)
        minans=min(minans,num)
        return
    if a-1>=0:
        do(num+nums[i],i+1,a-1,b,c,d)
    if b-1>=0:
        do(num-nums[i],i+1,a,b-1,c,d)
    if c-1>=0:
        do(num*nums[i],i+1,a,b,c-1,d)
    if d-1>=0:
        if num<0:
            tnum=num*(-1)
            tnum=tnum//nums[i]*(-1)
            do(tnum,i+1,a,b,c,d-1)
        else:
            do(num//nums[i],i+1,a,b,c,d-1)

do(nums[0],1,op[0],op[1],op[2],op[3])    
print(maxans)
print(minans)
