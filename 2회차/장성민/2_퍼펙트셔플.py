import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    card = list(input().split())

    if N % 2 == 0:
        half = N // 2
    if N % 2 != 0:
        half = (N // 2) + 1

    card_1 = card[:half]
    card_2 = card[half:]

    result = []
    if N % 2 == 0:
        for i, j in zip(card_1, card_2):
            result.append(i)
            result.append(j)
    if N % 2 != 0:
        for i, j in zip(card_1, card_2):
            result.append(i)
            result.append(j)
        result.append(card_1[-1])
        
    print(f'#{tc}', *result)
    
    


    