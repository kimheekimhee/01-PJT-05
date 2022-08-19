import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11):
    n = int(input())
    # 박스 오름차순으로 정렬
    box = sorted(list(map(int, input().split())))
    for _ in range(n):
        # 정렬했으니 가장 큰 값이 가장 끝 인덱스, 가장 작은 값이 가장 첫 인덱스
        # 하나씩 더하고 뺄 때마다 정렬
        box.sort()
        box[-1] -= 1
        box[0] += 1
    # 끝값에 1 빼고 첫값에 1 더하면서 반복문 종료됐으니까 최소, 최대값은 각각 앞뒤에서 두번째 숫자들
    # 최대값 - 최소값
    print(f'#{test_case}', box[-2] - box[1])