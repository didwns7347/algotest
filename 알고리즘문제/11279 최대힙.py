import sys
fin=0
n=int(input())
heap=[0 for x in range(100002)]
def hpop():
    global fin
    if fin==0:
        return 0
    ans=heap[1]
    heap[1]=heap[fin]
    heap[fin]=0
    fin-=1
    s=1
    while True:
        if s>=fin:
            break
        if heap[s]>heap[s*2] and heap[s]>heap[s*2+1]:
            break
        elif heap[s*2]>heap[s*2+1]:
            heap[s],heap[s*2]=heap[s*2],heap[s]
            s=s*2
        else:
            heap[s],heap[s*2+1]=heap[s*2+1],heap[s]
            s=s*2+1
    return ans

def insert(x):
    global fin
    fin+=1
    heap[fin]=x
    s=fin
    while True:
        if s==1:
            break
        if heap[s]>heap[s//2]:
            heap[s],heap[s//2]=heap[s//2],heap[s]
        s=s//2
    
    
for x in range(n):
    m=int(sys.stdin.readline())
    if m==0:
        print(hpop())
    else:
        insert(m)
    
