n=int(input())
import sys
def quick_sort(nums,s,f):
    if s>=f:
        return
    mid=(s+f)//2
    
    print(nums,mid,nums[mid],s,f)
    tmp=f+1
    while s<mid:
        if nums[s]>=nums[mid]:
            while tmp>=mid:
                tmp-=1
                if nums[tmp]<=nums[mid]:
                    nums[s],nums[tmp]=nums[tmp],nums[s]
                    break
        s+=1
    print(nums,mid,nums[mid])
    quick_sort(nums,s,mid)
    quick_sort(nums,mid+1,f)

nums=[]
for x in range(n):
    tmp=int(sys.stdin.readline().strip())
    nums.append(tmp)
quick_sort(nums,0,len(nums)-1)
for x in nums:
    print(x)

