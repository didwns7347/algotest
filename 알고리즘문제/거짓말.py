from sys import stdin
import sys

input=stdin.readline
n,m=map(int,input().split())
solomon=set(list(map(int,input().split()))[1:])
pts=[]
answer=[]
for x in range(m):
    party=list(map(int,input().split()))
    pts.append(party[1:])
    answer.append(1)


for _ in range(m):
    for i,party in enumerate(pts):
        if solomon.intersection(party):
            answer[i]=0
            solomon=solomon.union(party)

print(sum(answer))

    

        
        

            
        
