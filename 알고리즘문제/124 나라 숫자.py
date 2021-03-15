def solution(n):
    fot="4124"
    answer = ''
    while True:
        if n<=3:
            answer=fot[n]+answer
            break
        answer=fot[n%3]+answer
        if n%3==0:
            n=(n//3)-1
        else:
            n=n//3
    return answer


for i in range(1,50):
    print(solution(i))
