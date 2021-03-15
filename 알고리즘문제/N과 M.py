import itertools

N, M = map(int, input().split())
num_list = list(map(int,input().split()))
num_list.sort()
    
for num in itertools.combinations_with_replacement(num_list, M):
    for i in num:
        print(i, end = ' ')
    print(end = '\n')
