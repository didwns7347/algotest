from itertools import permutations
def solution(n, weak, dist):
    case=list(permutations(dist,len(dist)))
    aswer=0
    for test in case:
        solve(weak,test)
    return answer
def solve(weak,dist):
    cnt=0
    for x in range(len(weak)):
        
solution(12,	[1, 5, 6, 10],	[1, 2, 3, 4])
