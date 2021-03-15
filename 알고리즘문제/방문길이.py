def solution(dirs):
    answer = 0
    ans=set()
    x,y="F","F"
    for op in dirs:
        start=x+y
        if op=="U":
            if ord(y)+1<=75:
                y=chr(ord(y)+1)
            
        if op=="D":
            if ord(y)-1>=65:
                y=chr(ord(y)-1)
        if op=="R":
            if ord(x)+1<=75:
                x=chr(ord(x)+1)
        if op=="L":
            if ord(x)-1>=65:
                x=chr(ord(x)-1)
        
        nxt=x+y
        if start==nxt:
            continue
            
        ans.add(start+nxt)
    answer=len(ans)
    print(answer)
    return answer
solution("ULURRDLLU")
