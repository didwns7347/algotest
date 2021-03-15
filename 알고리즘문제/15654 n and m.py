from itertools import combinations
from itertools import permutations
n,m=map(int,input().split())
numlist=[x for x in range(1,n+1)]
numlist.sort()
out=list(combinations(numlist,m))
for x in range(len(out)):
    for y in out[x]:
        print(y,end=" ")
    print()
