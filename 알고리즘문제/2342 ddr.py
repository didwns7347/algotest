power=[[1,2,2,2,2],
       [0,1,3,4,3],
       [0,3,1,3,4],
       [0,4,3,1,3],
       [0,3,4,3,1]
       ]
op=list(map(int,input().split()))
op=op[:len(op)-1]
cost=0
l=op[0]
r=0
cost+=power[0][op[0]]

for x in range(1,len(op)):
  
    left=power[l][op[x]]
    right=power[r][op[x]]
    if left>right:
        cost+=right
        r=op[x]
    else:
        cost+=left
        l=op[x]
    

print(cost)
        
    
