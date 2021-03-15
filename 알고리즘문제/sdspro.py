if __name__=='__main__':
    n= int(input())
    cnt = 0
    j=[]
    h=[]
    while cnt<n:
        num=int(input())
        miro = [[int(x) for x in input().split()]for y in range(num)]
        jmap=[[0 for x in range(num)] for y in range(num)]
        hmap=[[0 for x in range(num)] for y in range(num)]
        if miro[0][0]%2==0:
                jmap[0][0]=1
                hmap[0][0]=0
        for x in range(num):
            for y in range(num):
                if x==0 :
                    if miro[x][y]%2==0:
                        jmap[x][y]=1+jmap[x][y-1]
                        hmap[x][y]=hmap[x][y-1]
                    else:
                        jmap[x][y]=jmap[x][y-1]
                        hmap[x][y]=hmap[x][y-1]+1
                if y==0:
                    if miro[x][y]%2==0:
                        jmap[x][y]=1+jmap[x-1][y]
                        hmap[x][y]=hmap[x-1][y]
                    else:
                        jmap[x][y]=jmap[x-1][y]
                        hmap[x][y]=hmap[x-1][y]+1
                else:
                    if miro[x][y]%2==0:
                        jmap[x][y]=max(jmap[x-1][y],jmap[x][y-1])+1
                        if jmap[x-1][y]==max(jmap[x-1][y],jmap[x][y-1]):
                            hmap[x][y]=hmap[x-1][y]
                        else:
                            hmap[x][y]=hmap[x][y-1]
                    else:
                        jmap[x][y]=max(jmap[x-1][y],jmap[x][y-1])
                        if jmap[x-1][y] == max(jmap[x-1][y],jmap[x][y-1]):
                            hmap[x][y]=hmap[x-1][y]
                        else:
                            hmap[x][y]=hmap[x][y-1]
                        
        j.append(jmap[-1][-1])
        h.append(hmap[-1][-1])
        cnt+=1
    for x in range(n):
        print("#"+str(x+1),h[x],j[x])
