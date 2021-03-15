def solution(stones, k):
    answer=0
    s=0
    f=max(stones)
    while True:
        if s>f:
            break
        people=(f+s)//2
        print(people,s,f,check(stones,people,k))
        if check(stones,people,k):
            s=people+1
            answer=max(answer,people)
        else:
            f=people-1
    return answer
def check(stones,people,k):
    print()
    cnt=0
    for x in range(len(stones)):
        #print(stones[x]-people,end=' ')
        if stones[x]-people<=0:
            
            cnt+=1
            if cnt>=k:
                return False
        else:
            cnt=0
    return True
                
print(solution(	[2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
