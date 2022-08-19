import sys

sys.stdin = open("_퍼펙트셔플.txt")
# 카드뭉치가 주어지고 퍼펙트셔플후 카드를 출력하기
from collections import deque


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N = int(input())
    card = input().split() # len(card) = N 
    card = deque(card)
    
    print(f'#{test_case}', end = ' ')
    if N % 2 == 0:
        divided = []               #첫번째것 -> 1/2로 나눈것의 첫번째것 -> 2번째것 -> 1/2로 나눈것의 두번째것 -> ....
        shuffled = []
        for i in range(int(N / 2), N):      #카드를 반으로 나눔.
            divided.append(card[i])
            divided = deque(divided)
        for i in range(int(N / 2)):             # 기존카드와 반으로 나눈카드에서 가장위에있는것들을 하나씩 집어넣어줌
            shuffled.append(card.popleft())
            shuffled.append(divided.popleft())
        for i in shuffled:
            print(i, end = ' ')
       

    else:
        divided = []
        shuffled = []        
        for i in range(int(N / 2) + 1, N):
            divided.append(card[i])
            divided = deque(divided)                # (N/2) - 1 개의 인덱스가 있음
        
        for i in range(int(N / 2)):             
            shuffled.append(card.popleft())
            shuffled.append(divided.popleft())

        shuffled.append(card[0])        # 카드와 디바이디드의 인덱스 개수가 안맞아서 위의 과정을 거친후 카드의 첫번쨰 인덱스를 넣어줘야됨
        for i in shuffled:
            print(i, end = ' ')
    print()