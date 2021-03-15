import sys
code=sys.stdin.readline().strip()

#st=list(st)
code=list(code)
print(code)
su=[0 for x in range(len(code))]
for x in range(1,len(code)):
    s=code[0:x+1]
    print(s)
    cnt=0
    for y in range(x//2):
        if s[y]==s[len(s)-y-1]:
            cnt+=1
    su[x]=cnt

print(su)
