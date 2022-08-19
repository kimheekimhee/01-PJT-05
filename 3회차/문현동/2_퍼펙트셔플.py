import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    card_name = input().split()
    
    # 만약 2로 나눠서 나머지가 존재한다면 몫에 + 1 아니라면 그냥 몫만 사용
    half = (len(card_name) // 2) + 1 if (len(card_name) % 2) else len(card_name) // 2
    
    front_list = card_name[:half]
    back_list = card_name[half:]
    
    card_shuffle = []
    i = 0
    while i < N: # N 회 반복
        if i % 2 == 0: # 앞쪽부분부터 짝/홀 순으로 들어간다.
            card_shuffle.append(front_list.pop(0))
        else:
            card_shuffle.append(back_list.pop(0))
        i += 1
        
    print(f"#{test_case} ", end = '')
    print(*card_shuffle)