import itertools

N, M = map(int, input().split())
num_list = list(map(int,input().split()))
num_list.sort()
tmp=list(set(itertools.combinations_with_replacement(num_list, M)))
tmp.sort()
    
for num in tmp:
    for i in num:
        print(i, end = ' ')
    print(end = '\n')
