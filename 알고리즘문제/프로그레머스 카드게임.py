#1. 언제든지 왼쪽 카드만 통에 버릴 수도 있고 왼쪽 카드와 오른쪽 카드를 둘 다 통에 버릴 수도 있다. 이때 얻는 점수는 없다.
#2. 오른쪽 카드에 적힌 수가 왼쪽 카드에 적힌 수보다 작은 경우에는 오른쪽 카드만 통에 버릴 수도 있다. 오른쪽 카드만 버리는 경우에는 오른쪽 카드에 적힌 수만큼 점수를 얻는다.
#3. (1)과 (2)의 규칙에 따라 게임을 진행하다가 어느 쪽 더미든 남은 카드가 없다면 게임이 끝나며 그때까지 얻은 점수의 합이 최종 점수가 된다.
from collections import deque
def solution(left, right):
    left=deque(left)
    right=deque(right)
    dp=[0 for x in range(n)]
    answer=0
    while True:
        if not left or not right:
            break
        l=left[0]
        r=right[0]
        if l>r:
            answer+=right.popleft()
        else:
            left.popleft()
    while True
        
    
    return answer

l = [1, 1, 1, 1, 3]
r = [2, 3, 1, 1, 1]
print(solution(l,r))
