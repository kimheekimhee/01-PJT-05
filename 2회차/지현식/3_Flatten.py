import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11):
    # 평탄화 횟수
    dump = int(input())
    n = list(map(int, input().split()))

    # 평탄화 수가 남아있으면 게속 돌기 위한 while문
    while dump:
        # 가장 높은 곳을 찾아 내려주고
        n[n.index(max(n))] -= 1
        # 가장 낮은 곳을 찾아 올려주고
        n[n.index(min(n))] += 1
        # 평탄화 수 - 1
        dump -= 1
    # 그중 가장 높은 지점 과 낮은 지점의 차이
    print(f"#{test_case} {max(n) - min(n) }")