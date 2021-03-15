n,k=map(int,input().split())
js=[ x for x in range(1,n+1)]
out=[]
i=k-1
for x in range(n):
    out.append(js.pop(i))
    if not js:
        break
    i=(i+k-1)%len(js)
print("<",end='')
for x in range(len(out)):
    if x==len(out)-1:
        print(out[x],end='')
    else:
        print(out[x],end=', ')
print(">")
