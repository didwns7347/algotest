T = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

acm, bcm = {}, {}
for i in range(n):
    t = 0
    for j in range(i, n):
        t += a[j]
        if acm.get(t):
             acm[t] += 1
        else:
            acm[t] = 1

for i in range(m):
    t=0
    for j in range(i, m):
        t += b[j]
        if bcm.get(t):
            bcm[t] += 1
        else:
            bcm[t] = 1

ans=0
        
for _, i in enumerate(acm):
    if bcm.get(T-i):
        ans += (acm[i]*bcm[T-i])
print(ans)

