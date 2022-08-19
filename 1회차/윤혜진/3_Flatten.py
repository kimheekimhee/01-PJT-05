# D3-Flatten



# 입력
'''
<총 10개의 테스트 케이스>
1. 덤프 횟수
- 평탄화: 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업
- 덤프: 가장 높은 곳에 있는 상자를 가장 낮은 곳으로 옮기는 작업
- 1 <= 덤프 횟수 <= 1,000
- 주어진 덤프 횟수 이내에 평탄화가 완료되면, 더이상 덤프를 수행할 수 없게 되므로 그 때의 최고점과 최저점의 높이 차를 반환(주어진 data에 따라 0 또는 1이 됨)
2. 각 상자의 높이값
- 가로 길이는 항상 100
- 1 <= 상자의 높이 <= 100
'''



# 출력
'''
1. #{테스트 케이스} {테스트 케이스의 최고점과 최저점의 높이 차}
'''



# 코드
import sys

sys.stdin = open("input_text/_Flatten.txt")

T = 10
for test_case in range(1, T + 1):
    dump_cnt = int(input())
    heights = list(map(int, input().split()))
    
    cnt = 0
    while cnt < dump_cnt:
        # 최대 높이, 최소 높이 구하기 
        max_h, max_i = 0, None
        min_h, min_i = 100, None
        for i in range(100):
            if max_h <= heights[i]:
                max_h = heights[i]
                max_i = i
            if min_h >= heights[i]:
                min_h = heights[i]
                min_i = i
        
        # 제한 덤프 횟수 내에 평탄화가 끝나는 경우
        if max_h - min_h <= 1:
            break

        # 최대 높이 상자를 최소 높이 상자에 하나 옮기기
        heights[max_i] -= 1
        heights[min_i] += 1
        cnt += 1

    print(f'#{test_case}', max(heights) - min(heights))



# 실행결과(메모리:61,672 kb, 시간:166 ms)