from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache=[]
    if cacheSize==0:
        return 5*len(cities)
    for ct in cities:
        word=""
        for c in ct:
            if ord(c)>=97:
                word+=chr(ord(c)-32)
            else:
                word+=c
        print(word)
        if word in cache:
            answer+=1
            idx = cache.index(ct)
            tmp=cache[idx]
            for i in range(idx,len(cache)-1):
                cache[i]=cache[i+1]
            cache[-1]=tmp
        else:
            answer+=5
            if len(cache)==cacheSize:
                for i in range(len(cache)-1):
                    cache[i]=cache[i+1]
                cache[-1]=word

            else:
                cache.append(word)
                

    print(answer)            
    return answer

solution(3,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"])

solution(2,	["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"])

solution(3,	["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"])
