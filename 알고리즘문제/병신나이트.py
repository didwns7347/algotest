#1783 병든 나이트
h,w=map(int,input().split())

if h==1:
    print(1)
if h==2:
    print(min(4,(w+1)//2))
if h>=3:
    if w>=7:
        print(w-2)
    else:
        print(min(4,w))
 
