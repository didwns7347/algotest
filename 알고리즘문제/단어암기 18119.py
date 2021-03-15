from sys import stdin
input=stdin.readline

N,M=map(int,input().split())
word=[[0 for _ in range(26)] for _ in range(N)]

char=[ 1 for _ in range(26)]

    
for i in range(N):
    w=list(input().strip())
    for x in w:
        word[i][ord(x)-97]=1


out=[]
dec=set()
cnt=[0 for _ in range(N)]
answer=N
for i in range(M):
    
    op,code=map(str,input().split())
    if op=="1":
        char[ord(code)-97]=0
        for j in range(N):
            if word[j][ord(code)-97]:
                if cnt[j]==0:
                    answer-=1
                cnt[j]-=1
        print(cnt)
            

    if op=="2":
        if char[ord(code)-97]==0:
            for k in range(N):
                if word[k][ord(code)-97]:
                    cnt[k]+=1
                   
                    if cnt[k]>=0:
                        answer+=1
        char[ord(code)-97]=1
        print(cnt)
        
    out.append(answer)
      
for x in out:
      print(x)
