# import sys

# sys.stdin = open("_Flatten.txt")

# 가장 큰 값과 작은 값을 구한 후 큰 값은 빼고 작은 값은 더해서 차이가 0또는 1이 되거나 덤프 시행 횟수만큼 실행을 한 후 출력하는 문제
# while문을 끝내는 조건을 잘못 설정해서 6번 테스트 케이스가 잘못 나왔으나, 종료 조건을 새로 설정하여 맞았습니다.

# 10번의 테스트 케이스를 위해 1~11까지 설정
for test_case in range(1, 11):
    # 덤프 시행 횟수
    dump_n = int(input())
    # 상자 높이들을 입력 받음
    list_ = list(map(int, input().split()))

    # 덤프를 더 이상 할 수 없을 때까지 반복
    while dump_n != -1:
        # max 값을 찾고
        max_ = max(list_)

        # min값을 찾은 뒤
        min_ = min(list_)

        # 둘의 차이를 구해서 새로운 변수에 저장 후
        gap_ = max_ - min_

        # 차 변수가 0 또는 1이면 종료
        if gap_ == 0 or gap_ == 1:
            break

        # 0또는 1이 아닌 경우 
        else:

            # 높이가 같을 경우 그 중 아무거나 옮길 수 있으므로 index를 활용해도 괜찮다.
            # max의 인덱스를 이용해 max -1, min의 인덱스를 이용해 min +1
            list_[list_.index(max_)] -= 1
            list_[list_.index(min_)] += 1

            # dump_n을 1 빼주고 반복
            dump_n -= 1

    # while문 다 돌고 난 후 혹은 break로 빠져나온 뒤 test_case와 max - min을 출력
    print(f'#{test_case} {gap_}')