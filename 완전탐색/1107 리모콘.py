import sys
sys.setrecursionlimit(2000)
n=input()
length=len(n)
n=int(n)
m=input()
nonum=list(map(int,input().split()))
def BF(num,l,numlen,cnt):
    print(num)
    if num==str(n):
        return cnt
    if l<numlen:
        for x in range(10):
            if x not in nonum:
                num=int(str(num)+str(x))
                return BF(num,l+1,numlen,cnt+1)
    if l==numlen and int(num)>n:
        return BF(num-1,l,numlen,cnt+1)
    elif int(num)<n:
        return BF(num+1,l,numlen,cnt+1)

print(min(BF('',0,length,0),abs(n-100)))