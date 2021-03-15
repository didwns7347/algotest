h,w=map(int,input().split())
m=[0,1,2,4,6,8]
if h>=3:
    ans=9*(w//6)+m[w%6]
    print(ans)
elif h==2:
    print(min(4,(w+1)//2
elif h==1:
    print(1)
