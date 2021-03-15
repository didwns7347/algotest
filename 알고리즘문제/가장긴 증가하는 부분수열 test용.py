import sys
from bisect import bisect_left
a=[1,2,3,4,5,5,6,7,8,9]
idx=bisect_left(a,5)
print(idx)

def solution():
    dp = [numbers[0]]
    res = [0]

    for i in range(1, n):

        if dp[-1] < numbers[i]:
            dp.append(numbers[i])
            res.append(len(dp)-1)
        else:
            idx = bisect_left(dp, numbers[i])
            dp[idx] = numbers[i]
            res.append(idx)
    print(res)
    print(dp)
    length = len(dp)
    print(length)
    result = []
    for i in range(len(res)-1, -1, -1):
        if res[i] == length-1:
            result.append(numbers[i])
            length -= 1
    print(*result[::-1])


n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
solution()
