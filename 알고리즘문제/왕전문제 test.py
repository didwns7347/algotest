N,S,D,F,B,K=map(int,input().split())
S1=S
if K > 0 :
    police=list(map(int,input().split()))
else :
    police=[]
cnt1=0
cnt2=0
i=[]
j=[]
while S!=D :
    if S < D :
        S=S+F
        if (S in police) or (S > N):
            S=S-F-B
        cnt1+=1
        if (i.count(S) >1) or (S < 1)or (S in police):
            cnt1=0
            break
        i.append(S)
    elif S > D :
        S=S-B
        if (S in police) or (S < 1):
            S=S+F+B
        cnt1+=1
        if (i.count(S) >1) or (S > N) or (S in police):
            cnt1=0
            break
        i.append(S)

while S1!=D :
    if S1 < D :
        S1=S1+F
        if (S1 > D)or(S1 in police) or (S1 > N):
            S1=S1-F-B
        cnt2+=1
        if (j.count(S1) >1) or (S1 < 1)or (S1 in police):
            cnt2=0
            break
        j.append(S1)
    elif S1 > D :
        S1=S1-B
        if (S1 < D)or(S in police) or (S < 1):
            S1=S1+F+B
        cnt2+=1
        if (j.count(S1) >1) or (S1 > N) or (S1 in police):
            cnt2=0
            break
        j.append(S1)
if cnt1==0 and cnt2 ==0 :
    print("BUG FOUND")
    #print(i,j,cnt1,cnt2,sep='\n')
elif cnt1 != 0 and cnt2 != 0 :
    print(min(cnt1,cnt2))
    #print(i,j,cnt1,cnt2,sep='\n')
else :
    print(max(cnt1,cnt2))
    #print(i,j,cnt1,cnt2,sep='\n')
