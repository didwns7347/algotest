import sys
n=int(input())
time=[]
for x in range(n):
    s,f=map(int,sys.stdin.readline().split())
    time.append([s,f])
time.sort(key=lambda x:(x[1],x[0]))

s,f=time[0][0],time[0][1]
cnt=1
for t in range(1,len(time)):
    if time[t][0]>=f:
        cnt+=1
        s=time[t][0]
        f=time[t][1]


print(cnt)
