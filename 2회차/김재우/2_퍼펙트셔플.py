import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card_list = list(map(str, input().split()))
    
    # 절반의 위치
    if N % 2 == 1:
        half = (N // 2) +1
    else:
        half = (N // 2) 
    
    # 절반으로 나눈 카드
    result_a = card_list[:half]
    result_b = card_list[half:]
    
    result = []

    # 카드를 한 곳에 (result) 모아주는 반복문
    for i in range(N):
        
        # range 벗어나지 않기 위한 조건

        if i < len(result_a):
            result.append(result_a[i])
        
        if i < len(result_b):
            result.append(result_b[i])

    # 출력 맞춤.
    result = ' '.join(result)

    print(f'#{tc} {result}')

# 조건을 계속 추가해서 코드가 지저분해졌습니다.. 리퀘스트 진행 후 고쳐보겠습니다.