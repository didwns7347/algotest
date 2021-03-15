parent=[x for x in range(200)]

def solution(n, computers):
    global parent
    answer = 0
    check=[0 for x in range(n)]
    for x in range(n):
        for y in range(n):
            if computers[x][y]==1:
                union(x,y)
    print(parent[0:n])
    for x in range(n):
        if check[parent[x]]==0:
            answer+=1
            check[parent[x]]=1

    return answer

def union(x,y):
    global parent
    x=find(x)
    y=find(y)
    parent[y]=x
def find(x):
    global parent
    if x==parent[x]:
        return x
    else:
        t=find(parent[x])
        parent[x]=t
        return t

c=[[1,0,0,1],[0,1,1,1],[0,1,1,0],[1,1,0,1]]
print("start")
print(solution(4,c))

