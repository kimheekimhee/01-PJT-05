import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 11):              # 10개의 테스트케이스
    dump = int(input())                     # 덤프 횟수
    box = list(map(int, input().split()))   # 100개의 박스 높이
    
    while dump:                             # 덤프 횟수가 끝날 때까지
        high = max(box)                     # 최고점
        row = min(box)                      # 최저점
        high_idx = box.index(high)          # 최고점 인덱스
        low_idx = box.index(row)            # 최저점 인덱스

        box[high_idx] -= 1                  # 최고점 박스 한 개 옮김
        box[low_idx] += 1                   # 최저점 박스 한 개 덤프

        dump -= 1                           # 덤프 횟수 1 차감

        height = max(box) - min(box)        # 최고점과 최저점 차이
        if height == 0 or height == 1:      # 덤프 횟수 이내에 평탄화 완료
            break                           # 덤프 종료

    print(f'#{test_case} {height}')         # 최고점과 최저점 차이 출력