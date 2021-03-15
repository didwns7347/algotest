k=100000000000
room_number=[1,3,4,1,3,1,9999999999,858999999]
def solution(k, room_number):
    answer = []
    MAX=max(room_number)
    room=[0 for x in range(MAX+len(room_number))]
    for x in room_number:
        if room[x]==0:
            room[x]=1
            answer.append(x)
        else:
            cnt=x
            while True:
                cnt+=1
                if room[cnt]==0:
                    room[cnt]=1
                    answer.append(cnt)
                    break
    return answer

print(solution(k,room_number))
