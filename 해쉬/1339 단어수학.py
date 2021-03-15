from itertools import permutations
n=int(input())
inputs=[]
aldic={}
answer=0
def next_permutation(a):
    n = len(a) - 1
    i = n
    while i > 0 and a[i-1] >= a[i]:
        i -= 1
    if i == 0: # 마지막 순열
        return False
    j = n
    while a[i-1] >= a[j]: # 오른쪽에 있으면서 a[i-1]보다 큰 수
        j -= 1
    a[i-1], a[j] = a[j], a[i-1] # SWAP
    j = n
    while i < j:
        a[i], a[j] = a[j], a[i] # a[i]부터 순열 뒤집기
        i += 1
        j -= 1
    return True
for x in range(n):
    s=input()
    s=list(s)
    inputs.append(s)
    for x in s:
        if x not in aldic:
            aldic[x]=0

nums=[i for i in range(9,9-len(aldic),-1)]
nums.reverse()

while True:
    if len(nums)!=1 and not next_permutation(nums):
        break
    cnt=0
    calc=[]
    for y in aldic:
        aldic[y]=nums[cnt]
        cnt+=1
    for a in inputs:
        tmp=''
        for b in a:
            tmp+=str(aldic[b])
        calc.append(int(tmp))
    answer=max(answer,sum(calc))
    if len(nums)==1:
        break
print(answer)