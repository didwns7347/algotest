n = int(input())
d = [0]*(n+1)
p = [0]+list(map(int, input().split()))

def solve():
    d[0], d[1] = 0, p[1]
    for i in range(2, n+1):
        for j in range(1, i+1):
            d[i] = max(d[i], d[i-j]+p[j])

solve()
print(d[n])


