n,m=map(int,input().split())
def factorial(n):
    if n==0:
        return 1
    elif n==1:
        return 1
    else:
        return n*factorial(n-1)

answer=factorial(n)/(factorial(m)*factorial(n-m))
print(int(answer))
