import sys
def solve(m,n,x,y):
    while x<=m*n:
        if x%n==y%n:
            return x
        x+=m
    return -1
        
for k in range(int(input())):
    m,n,x,y = map(int,input().split(" "))
    print(solve(m,n,x,y))
    
    

