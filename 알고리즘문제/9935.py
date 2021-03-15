import sys

st=input()
code=input()
st=list(st)
code=list(code)
out=[]
z=0
for x in range(len(st)):
    cnt=0
    out.append(st[x])

    if code[-1]==st[x]:
        for y in range(len(code)):
            if out[len(out)-y-1]==code[len(code)-y-1]:
                cnt+=1

    if cnt==len(code) :
        for x in range(cnt):
            out.pop()
    

if out:
    print(''.join(out).strip())
else:
    print("FRULA")
