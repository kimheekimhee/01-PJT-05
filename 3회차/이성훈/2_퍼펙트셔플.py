import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for j in range(1, T+1):

    N = int(input())
    Mid_N = (N // 2)
    list_1 = []


    list_ = input().split()

    if N % 2 == 0:
        for i in range(Mid_N):
            list_1.append(list_[i])
            list_1.append(list_[i + Mid_N])

    else:
        for i in range(Mid_N + 1):
            list_1.append(list_[i])
            if i == Mid_N :
                break
            list_1.append(list_[i + Mid_N + 1])


    print(f'#{j}', end = ' ')
    print(*list_1)