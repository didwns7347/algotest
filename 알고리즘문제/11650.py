import sys
sys.setrecursionlimit(100000)
n=int(input())

t=[]
for i in range(n):
    tmp=sys.stdin.readline().strip()
    x,y=map(int,tmp.split())
    t.append([x,y])

def part(t,l,r):
    tmp=t[r][0]
    tmpy=t[r][1]
    i=l
    for j in range(l,r):
        if t[j][0]<tmp:
            t[j],t[i]=t[i],t[j]
            i+=1
        if t[j][0]==tmp:
            if tmpy>t[j][1]:
                t[j],t[i]=t[i],t[j]
                i+=1
    t[i],t[r]=t[r],t[i]
    return i
def quicksort(t,l,r):
    if l<r:
        p=part(t,l,r)
        quicksort(t,l,p-1)
        quicksort(t,p+1,r)


quicksort(t,0,len(t)-1)
for x in t:
    print(x[0], x[1])
