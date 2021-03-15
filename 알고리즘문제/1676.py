n=int(input())
k=5
out=0
while True:
    if n//k==0:
        break
    out+=n//k
    n=n//5

print(out)
