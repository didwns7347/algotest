def solution(expression):
    op=[["+","-","*"],["+","*","-"]
        ["-","*","+"],["-","+","*"]
        ["*","-","+"],["*","+","-"]]
    
    for x in range(6):
        answer=max(answer,calc(expression,op[x]))
    return answer
                
num=["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(set(num))


