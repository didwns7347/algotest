#1541 잃어버린 괄호
t=input()
tmp=''
ss=[]
for x in range(len(t)):
    if t[x] not in ['+','-'] :
        tmp=tmp+t[x]
    else:
        ss.append(int(tmp))
        ss.append(t[x])
        tmp=''
    if x==len(t)-1:
        ss.append(int(tmp))
mcnt=0#마이너스 카운터
ans=[ss[0]]
for x in range(1,len(ss)):
    if ss[x]=="-":
        mcnt+=1    
    if type(ss[x])==int and mcnt!=0:
        ans.append(-1*ss[x])
    elif type(ss[x])==int and mcnt==0:
        ans.append(ss[x])
print(ans)
print(sum(ans))
