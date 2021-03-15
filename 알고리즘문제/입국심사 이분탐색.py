def solution(n, times):
    time=(n+1)*times[0]
    left=0
    right=time
    answer=0
    ans=[]
    while True:
        print(left,right)
        if left>=right:
            answer=left
            break
        mid=(left+right)//2
        people=0
        for t in times:
            people+=mid//t
        if people>n:
            right=mid-1
            ans.append(mid)
        if people==n:
            ans.append(mid)
            right=mid
        if people<n:
            left=mid+1
        
    
    return min(ans)
a=6
b=[7,10]
print(solution(6,b))
print(solution(10,[1,5]))
print(solution(1,[2,2]))
print(solution(3,[2,1,3]))
