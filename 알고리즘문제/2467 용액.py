n=int(input())
bot=list(map(int,input().split()))


s=0
f=len(bot)-1
answer=float("inf")
l=s
r=f
while True:
    if s==f:
        break
    if answer>abs(bot[s]+bot[f]):
        answer=abs(bot[s]+bot[f])
        l=s
        r=f
    
    if bot[s]<0 and bot[f]>0 :
        if abs(bot[s])>abs(bot[f]):
            s+=1
        else:
            f-=1
    elif bot[s]<0 and bot[f]<=0:
        s+=1
    elif bot[s]>=0 and bot[f]>0:
        f-=1
    else:
        break
    
print(bot[l],bot[r])
