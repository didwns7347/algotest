def solution(numbers, hand):
    t=[[0,0],[0,1],[0,3],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2]]
    llast=[3,0]
    rlast=[3,2]
    for x in range(len(nubers)):
        if numbers[x] in [1,4,7]:
            answer+="L"
            llast=t[nubers[x]]
        elif numbers[x] in [3,6,9]:
            answer+="R"
            rlast=t[numbers[x]]
        else:
            ldist=abs(t[numbers[x]][0]-llast[0])+abs(t[numbers[x]][1]-llast[1]) 
            rdist=abs(t[numbers[x]][0]-rlast[0])+abs(t[numbers[x]][1]-rlast[1])
            if ldist==rdist:
                if hand=="left":
                    answer+="R"
                    llast=t[numbers[x]]
                if hand=="right":
                    answer+="R"
            elif ldist>rdist:
                answer+="L"
                llast=t[numbers[x]]
            else:
                answer+="R"
                rlast=t[numbers[x]]
                

    answer = ''
    return answer
