v,e=map(int,input().split())
grap=[[0 for x in range(v+1)] for y in range(v+1)]
for x in range(e):
    a,b=map(int,input().split())
    grap[a][b]=1
    
