def solution(stones, k):
    people = 0
    fin=False

    while True:
        people+=1
        print(stones)
        cnt=0
        for x in range(len(stones)):
            stones[x]-=1
            if stones[x]<=0:
                cnt+=1
            else:
                if cnt>k:
                    fin=True
                else:
                    cnt=0
        if fin:
            break
        
    return people-1

s=[2, 2, 2, 3, 2, 1, 4, 2, 5, 1]
k=3
print(solution(s,k))
