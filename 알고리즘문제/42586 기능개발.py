def solution(progresses, speeds):
    progresses.reverse()
    speeds.reverse()
    answer = []
    while progresses:
        print(progresses)
        cnt=0
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
        while progresses:
            if progresses[-1]>=100:
                progresses.pop()
                cnt+=1
            else:
                if cnt!=0:
                    answer.append(cnt)
                break
    
    return answer
a=[95,90,99,99,80,99]
b=[1,1,1,1,1,1]
print(solution(a,b))
