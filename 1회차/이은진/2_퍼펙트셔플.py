import sys
from collections import deque
sys.stdin = open("_퍼펙트셔플.txt")

for t in range(1, int(input())+1):
    card_len = int(input())
    if card_len % 2 == 0:
        card = list(input().split())
        slicing = int((card_len / 2))
        card_1 = deque(card[:slicing])
        card_2 = deque(card[slicing:])
        suffle = []
        while card_2:
            suffle.append((card_1.popleft()))
            suffle.append((card_2.popleft()))
        a = ' '.join(suffle)
        print(f'#{t} {a}')
    else:
        card = list(input().split())
        slicing = int((card_len / 2)+1)
        card_1 = deque(card[:slicing])
        card_2 = deque(card[slicing:])
        suffle = []
        while card_1:
            suffle.append((card_1.popleft()))
            if len(card_2) != 0:
                suffle.append((card_2.popleft()))
        a = ' '.join(suffle)
        print(f'#{t} {a}')
