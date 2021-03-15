import sys
n,m=map(int ,input().split())
nums=['1','2','3','4','5','6','7','8','9']
pkl=[]
pkd={}
for x in range(n):
    tmp=sys.stdin.readline().strip()
    pkl.append(tmp)
    pkd[tmp]=x+1

for x in range(m):
    st=sys.stdin.readline().strip()
    if st[0] in nums:
        print(pkl[int(st)-1])
    else:
        print(pkd[st])
