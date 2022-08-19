import sys

sys.stdin = open("_퍼펙트셔플.txt")

from collections import deque

T = int(input())
for t in range(1, T + 1):
    last = ''
    N = int(input())
    cards = input().split()
    # print(cards)

    # 카드를 두 파트로 나누기
    horiz = len(cards) // 2
    
    card1 = cards[0:horiz]
    card2 = cards[horiz::]
    
# 홀수 개라면
    if len(cards) % 2 != 0:
        card1 = cards[0:horiz + 1]
        card2 = cards[horiz + 1::]
        last = card1.pop()

    card1 = deque(card1)
    card2 = deque(card2)

    answer = []
    for _ in range(horiz):
        num1 = card1.popleft()
        num2 = card2.popleft()
        
        answer.append(num1)
        answer.append(num2)
    
    if last != '':    
        answer.append(last)
    
    shuffle = ''
    for card in answer:
        shuffle += card + " "
        
    print(f'#{t} {shuffle}')