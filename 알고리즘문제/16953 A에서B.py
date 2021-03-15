from collections import deque
n,tg=map(int,input().split())
answer=float("inf")

q=deque()
q.append(n)
def BF(num,i):
    global answer
    if num>tg:
        return
    if num==tg:
        answer=min(answer,i)
        return
    BF(num*2,i+1)
    BF(num*10+1,i+1)
BF(n,0)
if answer==float("inf"):
    print(-1)
else:
    print(answer+1)
