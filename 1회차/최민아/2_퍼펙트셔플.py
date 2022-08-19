import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())                                    # 테스트케이스 개수

for test_case in range(1, T+1):
    N = int(input())                                # 카드 개수
    card = list(input().split())                    # N개의 카드 이름

    if N % 2 == 0:                                  # 짝수 장일 때
        idx = N//2                                  # 나누는 기준
    else:                                           # 홀수 장일 때
        idx = (N//2) + 1                            # 나누는 기준
    
    deck_1 = card[:idx]                             # 덱1
    deck_2 = card[idx:]                             # 덱2
    
    shuffle = []                                    # 셔플덱
    while True:
        if len(deck_1) != 0:                        # 덱1에 카드가 있으면
            shuffle.append(deck_1.pop(0))           # 덱1 카드 한 장 뽑음
        if len(deck_2) != 0:                        # 덱2에 카드가 있으면
            shuffle.append(deck_2.pop(0))           # 덱2 카드 한 장 뽑음
        if len(deck_1) == 0 and len(deck_2) == 0:   # 카드를 모두 뽑으면
            break                                   # 반복문 종료
    
    print(f'#{test_case}', end=' ')
    print(*shuffle)                                 # 셔플덱 출력