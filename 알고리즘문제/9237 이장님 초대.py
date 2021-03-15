n=int(input())
maokai=list(map(int,input().split()))

maokai.sort()
cnt=0
out=0
for x in range(n,0,-1):
    maokai[cnt]=maokai[cnt]+x
    out=max(out,maokai[cnt])
    cnt+=1
print(out+1)
