import sys

sys.stdin = open("_Flatten.txt")

T = 10 # 테스트 케이스 개수

for test_case in range(T):
    N = int(input()) # 덤프횟수
    heights = list(map(int, input().split())) # 높이들을 저장할 리스트

    for i in range(N): # 덤프횟수 만큼 반복
        if max(heights) - min(heights) > 1: # 최대 높이와, 차이가 1초과면
            heights[heights.index(max(heights))] -= 1 # 최대 -1
            heights[heights.index(min(heights))] += 1 # 최소 +1
        else: # 최대높이와 최소높이 차가 1이하면
            break
    print(f'#{test_case+1} {max(heights) - min(heights)}') # 최대 최소의 차 출력