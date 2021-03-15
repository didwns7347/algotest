n=int(input())
def hanoi(n,a,b,c):
    if n==1:
        print(a,c)
    else:
        hanoi(n-1,a,c,b)
        print(a,c)
        hanoi(n-1,b,a,c)
answer=0
for x in range(1,n+1):
    hanoi(n,1,2,3)