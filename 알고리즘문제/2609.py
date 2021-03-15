a,b=map(int,input().split())
aa,bb=a,b

g=0
h=0
while True:
    if a>b:
        a=a-b
    elif a<b:
        b=b-a
    else:
        g=a
        break
aa=aa//g
bb=bb//g
    
h=aa*bb*g
print(g)
print(h)
