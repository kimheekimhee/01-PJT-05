from operator import index
import sys

sys.stdin = open("_Flatten.txt")




for i in range(1, 11):

    N = int(input())

    N_list = list(map(int, input().split()))


    for _ in range(N):

        max_N_list_index = N_list.index(max(N_list))
        min_N_list_index = N_list.index(min(N_list))
        max_N_list = N_list[max_N_list_index]
        min_N_list = N_list[min_N_list_index]

        N_list[max_N_list_index] = max_N_list - 1
        N_list[min_N_list_index] = min_N_list + 1
        

    max_N_list_index = N_list.index(max(N_list))
    min_N_list_index = N_list.index(min(N_list))
    max_N_list = N_list[max_N_list_index]
    min_N_list = N_list[min_N_list_index]

    print(f'#{i} {max_N_list-min_N_list}')

    