import sys
sys.setrecursionlimit(2000)
room_dic={}
def solution(k, room_number):
    global room_dic
    answer = []
    for x in room_number:
        if x not in room_dic :
            room_dic[x]=x+1
            answer.append(x)
        else:
            nroom=find(x)
            room_dic[x]=nroom
            room_dic[nroom]=nroom+1
            answer.append(nroom)
    
    return answer
def find(x):
    if room_dic[x] not in room_dic:
        return x+1
    else:
        a=find(room_dic[x])
        room_dic[x]=a
        return a
print(solution(10,[1,3,4,1,3,1]))