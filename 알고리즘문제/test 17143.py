a,b=map(int,input().split())
aa=[]
aa.append(0)
aaa=[]
aaa.append(0)
ck=True
tmp=a
for x in range(2000):
    if ck:
        
        aa.append(tmp)
        tmp-=1
        if tmp==1:
            ck=False
    else:
        aa.append(tmp)
        tmp+=1
        if tmp==a:
            ck=True
tmp=1
ck=False
for x in range(2000):
    if ck:
        aaa.append(tmp)
        tmp-=1
        if tmp==1:
            ck=False
    else:
        aaa.append(tmp)
        tmp+=1
        if tmp==a:
            ck=True
print(aa[0:200])
        
print(aa[3+8])
