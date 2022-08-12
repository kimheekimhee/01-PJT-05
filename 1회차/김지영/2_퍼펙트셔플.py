# 카드 덱 정확히 절반으로 나누고
# 교대로 카드를 뽑아 새로운 덱 만들기

# input line
# T
# N # card count
# card = list(input().split())

# output line
# #{test_case} {string ' '.join(card_sort)}
import sys
sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for test_case in range(1,T+1):
    N = int(input())
    card = list(input().split())
    if len(card) % 2 == 0:
        card_1 = card[:len(card)//2]
        card_2 = card[len(card)//2:]
    else :
        card_1 = card[:len(card)//2+1]
        card_2 = card[len(card)//2+1:]
    # print(card_1,card_2)
    card_suffle = []
    for i in range(N):
        # print(card_suffle)
        if i % 2 == 0:
            card_suffle.append(card_1.pop(0))
        if i % 2 == 1 : 
            card_suffle.append(card_2.pop(0))
    result = ' '.join(card_suffle)
    print(f'#{test_case} {result}')