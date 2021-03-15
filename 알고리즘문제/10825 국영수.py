import sys
n=int(input())
slist=[]
class Student:
    def __init__(self,name,kor,eng,math):
        self.name=name
        self.kor=kor
        self.eng=eng
        self.math=math

for x in range(n):
    name,kor,eng,math=map(str,sys.stdin.readline().strip().split())
    slist.append(Student(name,int(kor),int(eng),int(math)))

slist.sort(key=lambda x:(-x.kor,x.eng,-x.math,x.name))

for x in slist:
    print(x.name)
