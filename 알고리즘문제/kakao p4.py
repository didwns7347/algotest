def solution(words, queries):
    cnt=0
    ans=0
    answer = []
    for x in queries:
        for y in words:
            cnt=0
            if len(x) == len(y):
                for a in range(0,len(x)):
                    print(x[a],y[a])
                    if x[a] == y[a] or x[a]=='?':
                        cnt+=1
                    else:
                        break
            if cnt == len(x):
                ans+=1
                
        print(x)
        answer.append(ans) 
        
        ans=0
                       

                        

    
    return answer

words=["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries=["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words,queries))
