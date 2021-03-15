N, K = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(N)]

weights = [ele[0] for ele in wv]
values = [ele[1] for ele in wv]
print(weights)
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, K+1):
        w = weights[i-1]
        v = values[i-1]
        if(j < w):
            dp[i][j] = dp[i-1][j]

        else:
            dp[i][j] = max(v + dp[i-1][j - w], dp[i-1][j])
print(dp[N][K])
