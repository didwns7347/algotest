import sys
import copy
n=int(input())
nums=list(map(int,input().split()))
num=copy.deepcopy(nums)

num=set(num)
num=list(num)
num.sort()
numdict={}
for x in range(len(num)):
    numdict[num[x]]=x
for x in nums:
    print(numdict[x],end=' ')
