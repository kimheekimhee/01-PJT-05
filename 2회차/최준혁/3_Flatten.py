# import sys

# sys.stdin = open("_Flatten.txt")

for t in range(1, 11): # 10번의 테스트 케이스
    N = int(input()) # 덤프 횟수
    box_hight = list(map(int, input().split())) # 상자의 높이값

    for i in range(N): # 덤프횟수만큼
        max_idx = box_hight.index(max(box_hight)) # 입력된 박스 높이의 최고점 인덱스
        min_idx = box_hight.index(min(box_hight)) # 입력된 박스 높이의 최저점 인덱스
        box_hight[max_idx] -= 1 # 박스 최고점에서 1개씩 차감
        box_hight[min_idx] += 1 # 박스 최저점에서 1개씩 증가

    # 테스트케이스와 최고점에서 최저점을 뺀 값(차이) 출력
    print("#{} {}".format(t, max(box_hight)-min(box_hight)))