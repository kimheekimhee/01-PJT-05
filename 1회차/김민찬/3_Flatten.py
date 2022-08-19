import sys

sys.stdin = open("_Flatten.txt")

TC = 10 # 테스트 케이스의 개수 = 10
for i in range(1, 11):
    T = int(input()) # 상자 이동 가능 횟수
    box = list(map(int, input().split())) # 상자 배열 = box

    for j in range(T):
        max_index = box.index(max(box))
        min_index = box.index(min(box))
        box[max_index] -= 1 # 최댓값 index 값에서 1 빼기
        box[min_index] += 1 # 최솟값 index 값에서 1 더하기

    print("#{} {}".format(i, max(box) - min(box))) # 최댓값 - 최솟값 = 출력