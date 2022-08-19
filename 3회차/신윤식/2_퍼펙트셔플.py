import sys

sys.stdin = open("./3회차/신윤식/_퍼펙트셔플.txt")

T = int(input())

for _ in range(1, T+1):
    N = int(input())
    cards_lst = input().split()
    if N%2 == 0:
        cards_f = cards_lst[:(N//2)]
        cards_b = cards_lst[(N//2):]
    else:
        cards_f = cards_lst[:(N//2 + 1)]
        cards_b = cards_lst[(N//2 + 1):]

    print(f'#{_}', end = ' ')
    for i in range(N):
        if i % 2 == 0:
            print(cards_f[i//2], end=' ')
        elif i % 2 == 1:
            print(cards_b[i//2], end=' ')
    print()