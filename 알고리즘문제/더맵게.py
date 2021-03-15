def solution(str1, str2):
    a=list(str1)
    b=list(str2)
    ga=[]
    gb=[]
 
    for i in range(len(a)):
        if 97<=ord(a[i])<=122:
            a[i]=chr(ord(a[i])-32)
        if i !=0:
            if 65<=ord(a[i-1])<=90 and 65<=ord(a[i])<=90:
                ga.append(a[i-1]+a[i])
    for i in range(len(b)):
        if 97<=ord(b[i])<=122:
            b[i]=chr(ord(b[i])-32)
        if i!=0:
            if 65<=ord(b[i-1])<=90 and 65<=ord(b[i])<=90:
                gb.append(b[i-1]+b[i])
    print(ga,gb)
    answer=int(solve(ga,gb)*65536)
    return answer
def solve(a,b):
    go=0
    na=0
    ta=set()
    tb=set()
    for e in a:
        ta.add(e)
    for e in b:
        tb.add(e)
    hab=ta|tb
    gab=ta&tb
    print(hab)
    print(gab)
    for e in gab:
        na+=min(find(a,e),find(b,e))
    for e in hab:
        go+=max(find(a,e),find(b,e))
    print(na,go)
    return na/go
def find(mlist,key):
    cnt=0
    for x in mlist:
        if x==key:
            cnt+=1
    return cnt
solution("handshake","shake hands")
