from collections import deque
import sys

sys.stdin = open("_퍼펙트셔플.txt")


t = int(input())

for i in range(1, t + 1):
    n = int(input())

    card = list(input().split())

    cut = n - (n // 2)
    f_card = deque(card[:cut])
    s_card = deque(card[cut:])

    result = []
    while f_card or s_card:
        if f_card:
            result.append(f_card.popleft())
        if s_card:
            result.append(s_card.popleft())

    print(f'#{i}', end=' ')
    print(*result)
