from collections import deque
import copy
n=int(input())
board=[]
ans=0
    
for x in range(n):
    board.append(list(map(int,input().split())))
def left(c):
    m=copy.deepcopy(c)
    global ans
    for x in range(n):
        q=deque()
        for y in range(n):
            if m[x][y]!=0:
                q.append(m[x][y])
                m[x][y]=0
        i=0
        hap=True
        while True:
            if not q:
                break
            tmp=q.popleft()
            if m[x][i]==0:
                m[x][i]=tmp
                hap=True
            else:
                if m[x][i]==tmp and hap:
                    m[x][i]+=tmp
                    hap=False
                else:
                    i+=1
                    m[x][i]=tmp
                    hap=True
    for x in m:
        ans=max(ans,max(x))
    return m
def right(c):
    m=copy.deepcopy(c)
    global ans
    for  x in range(n):
        q=deque()
        for y in range(n):
            if m[x][y]!=0:
                q.append(m[x][y])
                m[x][y]=0
        i=n-1
        hap=True
        while True:
            if not q:
                break
            tmp=q.pop()
            if m[x][i]==0:
                m[x][i]=tmp
                hap=True
            else:
                if m[x][i]==tmp and hap:
                    m[x][i]+=tmp
                    hap=False
                else:
                    i-=1
                    m[x][i]=tmp
                    hap=True
    for x in m:
        ans=max(ans,max(x))
    return m

def up(c):
    m=copy.deepcopy(c)
    global ans
    for x in range(n):
        q=deque()
        for y in range(n):
            if m[y][x]!=0:
                q.append(m[y][x])
                m[y][x]=0
        i=0
        hap=True
        while True:
            if not q:
                break
            tmp=q.popleft()
            if m[i][x]==0:
                m[i][x]=tmp
                hap=True
            else:
                if m[i][x]==tmp and hap:
                    m[i][x]+=tmp
                    hap=False
                else:
                    i+=1
                    m[i][x]=tmp
                    hap=True
    for x in m:
        ans=max(ans,max(x))
    return m

def dwon(c):
    m=copy.deepcopy(c)
    global ans
    for x in range(n):
        q=deque()
        for y in range(n):
            if m[y][x]!=0:
                q.append(m[y][x])
                m[y][x]=0
        i=n-1
        hap=True
        while True:
            if not q:
                break
            tmp=q.pop()
            if m[i][x]==0:
                m[i][x]=tmp
                hap=True
            else:
                if m[i][x]==tmp and hap:
                    m[i][x]+=tmp
                    hap=False
                else:
                    i-=1
                    m[i][x]=tmp
                    hap=True
    for x in m:
        ans=max(ans,max(x))
    return m



        
def do(m,x):
    if x==5:
        return
    
    do(left(m),x+1)
    do(right(m),x+1)
    do(up(m),x+1)
    do(dwon(m),x+1)
    
    

do(board,0)
print(ans)

    

                   
            
                    
                    
                    
                
        
                 
                
