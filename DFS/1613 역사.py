n,k = map(int,input().split())
before=[ [] for x in range(n+1)]
after=[ [] for x in range(n+1)]
answer=[]
for x in range(k):
    a,b=map(int,input().split())
    before[b].append(a)
    after[a].append(b)

def BeforeDFS(a,b):
    Bcheck[a]=True
    if a==b:
        answer.append(1)
        return True
    for x in before[a]:
        if Bcheck[x]==False:
            return BeforeDFS(x,b)
    return False

def AfterDFS(a,b):
    Acheck[a]=True
    if a==b:
        answer.append(-1)
        return True
    for x in after[a]:
        if Acheck[x]==False:
            return AfterDFS(x,b)
    return False

t=int(input())

for x in range(t):
    Acheck=[False for x in range(n+1)]
    Bcheck=[False for x in range(n+1)]
    a,b=map(int,input().split())
    if not AfterDFS(a,b) and  not BeforeDFS(a,b):
        answer.append(0)

for x in answer:
    print(x)