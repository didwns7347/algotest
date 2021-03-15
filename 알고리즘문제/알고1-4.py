n=int(input())
m=2*n-1

for x in range(n):
    k=(x+1)*2-1
    for y in range(m):
        if y>=n-x-1 and y<n-x-1+k:
            print("*",end='')
        if y<n-x-1:
            print(" ",end='')
    print()


    
