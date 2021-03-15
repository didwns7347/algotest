print("start")
n=int(input())
s=[]

def back_tracking(i):
    print("s= ",s)
    for m in range(1, (i//2) + 1):
        print(s[-m:],s[-2*m:-m])
        if s[-m:] == s[-2*m:-m]: 
            return -1
    if i==n:
        print("answer=: ",end='')
        for t in s:
            print(t,end='')
        return 0
    for x in range(1,4):
        s.append(x)
        if back_tracking(i+1)==0:
            return 0
        s.pop()
back_tracking(0)