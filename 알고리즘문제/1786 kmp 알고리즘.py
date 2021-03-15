st=list(input())
pt=list(input())
#print(st,pt)
p=[0 for _ in range(len(pt))]

j=0
for i in range(1,len(pt)):
    while j>0 and pt[i]!=pt[j]:
        j=p[j-1]
    if pt[i]==pt[j]:
        j+=1
        p[i]=j
#print(p)
answer=0
def comp(a,b):
    #print(a,b)
    cnt=0
    for x in range(len(b)):
        if a[x]!=b[x]:
            return cnt
        cnt+=1
    return cnt

x=0
out=[]
j=0
for i in range(0,len(st)):
    while(j>0 and st[i]!=pt[j]):
        j=p[j-1]
    if st[i]==pt[j]:
        if j==len(pt)-1:
            out.append(i-len(pt)+2)
            answer+=1
            j=p[j]
        else:
            j+=1
          
               
print(answer)
for x in out:
    print(x)
