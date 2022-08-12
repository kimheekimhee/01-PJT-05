import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input()) # 테스트 케이스 개수

for test_case in range(T):
    N = int(input()) # 카드 개수
    card_list = list(input().split()) # 카드들을 리스트로 저장
    a_list = [] # 앞쪽 절반을 저장할 리스트
    b_list = [] # 뒤쪽 절반을 저장할 리스트

    if N % 2 == 0: # 카드 개수가 짝수 일떄
        t = 0
    else:          # 카드 개수가 홀수 일떄
        t = 1

    for i in range(N): # 카드 개수만큼 순회
        if i < (N//2)+t: # 앞쪽 카드들 a_list에 저장
            a_list.append(card_list[i])
        else:            # 뒷쪽 카드들 b_list에 저장
            b_list.append(card_list[i])

    print(f'#{test_case+1} ', end ='') # 하나씩 빼면서 출력
    while len(b_list) != 0:
        print(a_list[0], end=' ')
        a_list.pop(0)
        print(b_list[0], end=' ')
        b_list.pop(0)
    if t == 1:
        print(a_list[0], end=' ')
    print()