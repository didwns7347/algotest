def solution(record):
    answer = []
    id_dic={}
    for s in record:
        s=s.split()
        if s[0]=="Enter":
            id_dic[s[1]]=s[2]
        elif s[0]=="Leave":
            continue
        else:
            id_dic[s[1]]=s[2]
    for s in record:
        s=s.split()
        if s[0]=="Enter":
            text=id_dic[s[1]]+"님이 들어왔습니다."
            answer.append(text)
        elif s[0]=="Leave":
            text=id_dic[s[1]]+"님이 나갔습니다."
            answer.append(text)
        else:
            continue
    return answer

r=["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

a= solution(r)
for s in a:
    print(s)
