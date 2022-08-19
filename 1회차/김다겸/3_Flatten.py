import sys

sys.stdin = open("_Flatten.txt")

for t in range(1, 11):
    n = int(input())
    box = list(map(int, input().split()))

    for i in range(n):
        # box에서 max와 min 저장
        max_ = max(box)
        min_ = min(box)
        # box 순회
        for j in range(len(box)):
            # box의 값이 max와 같으면
            if box[j] == max_:
                # 해당 값에서 1 빼기
                box[j] -= 1
                # 중단
                break
        # box 순회
        for l in range(len(box)):
            # box의 값이 min과 같으면
            if box[l] == min_:
                # 해당 값에서 1 더하기
                box[l] += 1
                # 중단
                break
    # box의 가장 높은 값에서 가장 낮은 값 빼기
    print(f'#{t} {max(box) - min(box)}')