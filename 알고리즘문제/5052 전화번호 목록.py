from sys import stdin
input= stdin.readline
def check(num,i,ck):
    print(tree[i][int(num[i])],ck)
    if ck:
        if not tree[i][int(num[i])] and i!=len(num)-1:
            global answer
            answer=False
            print(i)
            return
    if i==len(num)-1:
        return
    if int(num[i+1]) not in tree[i][int(num[i])]:
        tree[i][int(num[i])].append(int(num[i+1]))
    return check(num,i+1,ck)
for _ in range(int(input())):
    n=int(input())
    tree=[[[] for _ in range(10)] for _ in range(10)]
    nlist=[]
    for _ in range(n):
        num=list(input().strip())
        nlist.append(num)
    nlist.sort(key=len)
    for cnum in nlist:
        answer=True
        print(cnum)
        if int(cnum[1]) in tree[0][int(cnum[0])]:
            check(cnum,0,True)
        else:
            check(cnum,0,False)
        if not answer:
            print("NO")
            break
        for x in tree:
            print(x)
    if answer:
        print("YES")
