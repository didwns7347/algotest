g,b,i=map(int,input().split())
cnt=0
if b+g-i<3:
    print(0)
else:
    while True:
        b=b-1
        g=g-2
        if b<0 or g<0 or b+g<i:
            print(cnt)
            break
        
        cnt+=1
  
        
        
