import sys
class count:
    def __init__(self,age,name,num):
        self.age=age
        self.name=name
        self.num=num
    

n=int(input())
countlist=[]
for x in range(n):
    num=x
    age,name=(map(str,sys.stdin.readline().strip().split()))
    age=int(age)
    a=count(age,name,num)
    countlist.append(a)

countlist.sort(key=lambda x:(x.age,x.num))
for x in countlist:
    print(x.age,x.name)
