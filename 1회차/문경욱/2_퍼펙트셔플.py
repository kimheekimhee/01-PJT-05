# import sys

# sys.stdin = open("_퍼펙트셔플.txt")

# 리스트를 입력받은 것을 반으로 나눈 뒤 한 번씩 번갈아가면서 추가하는 방식을 사용했습니다.
# 리스트의 요소가 짝수개일 때는 간단했지만 홀수일 때는 인덱스 설정을 잘못해서 시간이 조금 걸렸습니다.

# 테스트 케이스 수 입력
T = int(input())
for test_case in range(1, 1+T):
    # 카드 수 입력
    N = int(input())
    list_ = list(map(str, input().split()))
    # 새로운 리스트 선언
    suffled_ = []

    # 리스트를 반으로 나누기
    # N이 짝수이면
    if N % 2==0:
        # 기존 리스트를 반으로 나눠 각각 새로운 리스트로 만들고
        half_N = int(N/2)
        list_A = list_[0:half_N]
        list_B = list_[half_N:N]
        # 번갈아가면서 하나씩 추가
        for i in range(half_N):
            suffled_.append(list_A[i])
            suffled_.append(list_B[i])

    # N이 홀수이면
    else:
        # 기존 리스트를 반으로 나눠야 하는데, 문제에서 먼저 놓은 것이 하나 더 들어가야 하므로 한 개 더 추가
        half_N = int(N/2)+1
        list_A = list_[0:half_N]
        list_B = list_[half_N:N]
    
        # 번갈아가면서 하나씩 추가
        for i in range(half_N-1):
            suffled_.append(list_A[i])
            suffled_.append(list_B[i])
        # 들어가지 못한 list_A에서 마지막 요소 추가
        suffled_.append(list_A[half_N-1])
 
    print(f'#{test_case}', end=' ')
    for i in suffled_:
        print(i, end=' ')
    print()