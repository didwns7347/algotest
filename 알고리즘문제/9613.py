#9613번
import sys
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

n=int(input())
for x in range(n):
    k=0
    t=sys.stdin.readline().strip()
    test=list(map(int,t.split()))
    num=test[0]
    test=test[1:]
    for x in range(num-1):
        for y in range(x+1,num):
            k=k+gcd(test[x],test[y])
    print(k)
