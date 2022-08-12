import sys

sys.stdin = open("_Flatten.txt")

T = 10
for t in range(1,T+1):
    n = int(input()) # 덤프 횟수
    box = list(map(int,input().split())) # 박스들

    # 덤프 횟수만큼 반복
    for j in range(n):
        # 가장 높은 박스의 인덱스 번호를 저장
        idx = box.index(max(box))
        # 가장 높은 박스 -1 해주고
        # 인덱스번호로 원래 위치에 재할당
        box[idx] = max(box) - 1

        # 가장 낮은 박스의 인덱스 번호 저장
        idx = box.index(min(box))
        # 가장 낮은 박스에 +1 해주고 원래 위치에 재할당
        box[idx] = min(box) + 1

    # 최고점, 최저점 높이차 출력
    print(f'#{t}', max(box)-min(box))