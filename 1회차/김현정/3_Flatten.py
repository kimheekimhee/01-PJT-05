import sys

sys.stdin = open("_Flatten.txt")

# 10개의 테스트 케이스가 주어짐
for _ in range(1, 11):
    # 덤프 횟수
    N = int(input())
    box_result = 0

    # 상자의 높이 값을 리스트로 변환, 높이 계산해야하므로 int형
    box_height = list(map(int, input().split()))

    while N+1:
        box_height.sort()
        box_height[len(box_height)-1] -= 1
        box_height[0] += 1
        N -= 1

    # 답을 맞추기 위해 +2를 넣긴했는데 왜 +2가 들어갔는지 이해를 못함
    box_result = box_height[len(box_height)-1] - box_height[0] + 2
    print(f"#{_}", box_result)