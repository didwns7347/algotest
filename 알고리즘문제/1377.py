import sys
n=int(input())
num=[0]
cnt=0
for x in range(1,n+1):
    tmp=sys.stdin.readline()
    tmp=int(tmp)
    num.append(tmp)
for x in range(1,n):
    if num[x]>num[x+1]:
        cnt+=1

print(cnt+1)
        
