#1080 행렬
import sys
cnt=0
def change(a,b):
    for x in range(a,a+3):
        for y in range(b,b+3):
            if m1[x][y]==0:
                m1[x][y]=1
            else:
                m1[x][y]=0
h,w=map(int,input().split())
m1=[list(map(int,list(input()))) for  x in range(h)]
m2=[list(map(int,list(input()))) for  x in range(h)]
for x in range(h-2):
    for y in range(w-2):
        if m1[x][y]!=m2[x][y]:
            cnt+=1
            change(x,y)

for x in range(h):
    for y in range(w):
        if m1[x][y] != m2[x][y]:
            cnt=-1
            break
print(cnt)
