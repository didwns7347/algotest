n=12
weak=[1, 3, 4, 9, 10]
g=[weak[0]]
gg=[]
res=[]
start=0
lg=12-weak[start-1]+weak[start]
rg= weak[start+1]-weak[start]
l=0
left=0
right=0
while(True):
    if lg<rg:
        if weak[left-1] in g:
            break
        g.append(weak[left-1])
        gg.append([weak[left],weak[left-1]])
        l+=lg
        res.append(lg)
        left=left-1
        lg=weak[left]-weak[left-1]
    else :
        if weak[right+1] in g:
            break
        g.append(weak[right+1])
        gg.append([weak[right],weak[right+1]])
        l+=rg
        res.append(rg)
        right=right+1
        rg=weak[right+1]-weak[right]
    
print(l)
print(g)
print(res)
print(gg)
        
