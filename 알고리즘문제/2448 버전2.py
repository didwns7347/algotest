import math
s=["  *   "," * *  ","***** "]
def star(sft):
    c= len(s)
    for i in range(c):
        s.append(s[i]+s[i])
        s[i]=("   "*sft + s[i]+"   "*sft)
n=int(input())
k=int(math.log(n//3,2))
for i in range(k):
    star(int(pow(2,i)))
for i in range(n):
    print(s[i])
