a,p=map(int,input().split())

gg=[0]*236197

cnt=1
def amake(a):
    aa=[]
    while True:
        if a/10 < 1:
            aa.append(a)
            break
        aa.append(a%10)
        a=a//10
    aa.reverse()
    return aa
gg[a]=1
while True:
    c=0
    cnt+=1
    tmp=amake(a)
    for x in tmp:
        c+=x**p
    if gg[c]!=0:
        print(gg[c]-1)
        break
    else:
        gg[c]=cnt
        a=c

