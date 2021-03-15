import operator
n = int(input())
word=[]
aldic={}
answer=[]
for x in range(n):
    s=list(input())
    word.append(s)
for x in word:
    j=len(x)-1
    for s in x:
        if s not in aldic:
            aldic[s]=10**j
        else:
            if aldic[s]<10**j:
                aldic[s]=10**j
        j-=1

aldict=sorted(aldic.items(), key=operator.itemgetter(1),reverse=True)



num=9
for x in aldict:
    aldic[x[0]]=num
    num-=1
for x in word:
    tmp=''
    for s in x:
        tmp+=str(aldic[s])
    answer.append(int(tmp))
print(sum(answer))