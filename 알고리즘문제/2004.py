#조합0의 개수


def five(n):
    out=0
    while True:
        if n//5==0:
            break
        out+=n//5
        n=n//5
    return out
def two(n):
    out=0
    while True:
        if n//2==0:
            break
        out+=n//2
        n=n//2
    return out
        
n,m=map(int,input().split())
k=n-m
ten=five(n)-five(m)-five(k)
print(ten)
e=two(n)-two(m)-two(k)
print(e)
min(ten,e)
