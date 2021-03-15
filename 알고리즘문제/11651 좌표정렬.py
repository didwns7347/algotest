import sys
n=int(input())
t=[]
def select(t,l,r):
    i=l
    p=t[r]
    for j in range(l,r):
        if t[j][1]<p[1]:
            t[j],t[i]=t[i],t[j]
            i+=1
        if t[j][1]==p[1] and t[j][0]<p[0]:
            t[j],t[i]=t[i],t[j]
            i+=1
    t[i],t[r]=t[r],t[i]
    return i
def quick_sort(t,l,r):
    if l<r:
        p=select(t,l,r)
        quick_sort(t,l,p-1)
        quick_sort(t,p+1,r)
        
for x in range(n):
    tmp=list(map(int,sys.stdin.readline().strip().split()))
    t.append(tmp)


quick_sort(t,0,len(t)-1)
for x in t:
    print(x[0],x[1])
