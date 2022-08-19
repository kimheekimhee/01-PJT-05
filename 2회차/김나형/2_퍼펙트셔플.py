from re import L
import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(map(str, input().split()))

    if N % 2 == 0:
        card1 = card[:N//2]
        card2 = card[N//2:]
    else:
        card1 = card[:N//2 + 1]
        card2 = card[N//2 + 1:]
    # ['A', 'B', 'C'] ['D', 'E', 'F']
    # ['JACK', 'QUEEN'] ['KING', 'ACE']
    # ['ALAKIR', 'ALEXSTRASZA', 'DR-BOOM'] ['LORD-JARAXXUS', 'AVIANA']
    perpect = []

    while card1 or card2:
        if len(card1) != 0:
            perpect.append(card1.pop(0))
        if len(card2) != 0:
            perpect.append(card2.pop(0))
    
    print(f'#{tc}', *perpect)



