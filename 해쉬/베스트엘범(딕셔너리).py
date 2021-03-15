import operator
def solution(genres, plays):
    answer = []
    musicg={}
    music={}
    for i,g in enumerate(genres):
        music[i]=[g,plays[i]]
        if not musicg.get(g):
            musicg[g]=plays[i]
        else:
            musicg[g]+=plays[i]
    musicg=sorted(musicg.items(),
            key=lambda item: item[1]
            ,reverse=True)
  
    music=sorted(music.items(),
            key=lambda item: item[1][1]
            ,reverse=True)


    for x in musicg:
        cnt=0
        for y in music:
            if x[0]==y[1][0]:
                answer.append(y[0])
                cnt+=1
            if cnt==2:
                cnt=0
                break
    return answer
    

a=["classic", "pop", "classic", "classic", "pop"]
a2=["classic", "pop", "classic", "classic", "pop"]
b2=[500, 600, 501, 800, 900]
b=[500,1000, 150, 1600, 2500]
print(solution(a,b))
print(solution(a2,b2))