import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    S = list(input().split())
    div = N // 2
    print(f'#{test_case} ', end='')
    for i in range(div):
        if N % 2 == 1:
            print(S[i], S[div + 1], end=' ')
        else:
            print(S[i], S[div], end=' ')
        div += 1
    if N % 2 == 1:
        div = N // 2
        print(S[div])
    else:
        print()