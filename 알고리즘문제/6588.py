import sys
out=[]

num=[1 for x in range(0,1000001)]
ss=[]

for i in range(2,500000):
    if num[i]:
        for j in range(2,1000001):
            if i*j>1000000:
                break
            num[i*j]=0

for x in range(2,len(num)):
    if num[x]!=0:
        ss.append(x)

while True:
    n=sys.stdin.readline().strip()
    n=int(n)
    if n==0:
        break
    
    for x in ss:
        t=n-x
        if t>1 and num[t]!=0:
            st=str(n)+" "+"="+" "+str(x)+" "+"+"+" "+str(t)
            out.append(st)
            break
for x in out:
    print(x)
