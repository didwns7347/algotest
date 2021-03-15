n=int(input())
pn=[2,3,5,7]
def boolpn(n):
    for x in range(2,int(n**0.5)+1):
        if n%x==0:
            return False
    return True


def backt(i,num):
    if i==n:
        print(num)
        return
    for x in range(1,10):
        if boolpn(int(str(num)+str(x))):
            backt(i+1,int(str(num)+str(x)))
        
for x in pn:
    backt(1,x)