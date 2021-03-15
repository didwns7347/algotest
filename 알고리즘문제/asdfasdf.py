def solution(n):
    answer = 0
    nums=[1 for x in range(n+1)]
    for x in range(2,n//2+1):
        if nums[x]==1:
            for y in range(2,n):
                if x*y>n:
                    break
                nums[x*y]=0
    print(nums)
    for x in range(2,n+1):
        if nums[x]==1:
            answer+=1
    return answer
print(solution(5))
