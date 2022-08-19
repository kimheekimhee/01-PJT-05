import sys

sys.stdin = open("_퍼펙트셔플.txt")
from collections import deque

T = int(input())
for ts in range(1, T+1):
    N = int(input())
    card = input().split()
    new_card = deque([])
    if N % 2 == 0:
        card1 = deque(card[:N//2])
        card2 = deque(card[N//2 :])
        for a in range(N//2):
            new_card.append(card1.popleft())
            new_card.append(card2.popleft())
    else: 
        card1 = deque(card[:N//2 +1])
        card2 = deque(card[N//2 +1:])
        for a in range(N//2):
            new_card.append(card1.popleft())
            new_card.append(card2.popleft())
        new_card.append(card1.popleft())
        
    print(f"#{ts} {' ' .join(new_card)}")