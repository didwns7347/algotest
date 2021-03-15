n=list(input())
check=False
for x in range(len(n)):
    n[x]=int(n[x])
    if n[x]==0:
        check=True
if not check:
    print(-1)

else:
    if sum(n)%3==0:
        n.sort()
        n.reverse()
        for x in n:
            print(x,end='')
    else:
        print(-1)
