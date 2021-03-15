board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
print(len(board))
for x in board:
    print(x)
from collections import deque
def solution(board, moves):
    st=deque()
    answer = 0
    for x in moves:
        tmp=-1
        for y in range(len(board)):
            if board[y][x-1]!=0:
                tmp=board[y][x-1]
                board[y][x-1]=0
                break
        if tmp==-1:
            continue
        else:
            if st:
                if st[-1]==tmp:
                    st.pop()
                    answer+=2
                else:
                    st.append(tmp)
            else:
                st.append(tmp)
    print(st)
    for x in board:
        print(x)


    return answer

print(solution(board, moves))
