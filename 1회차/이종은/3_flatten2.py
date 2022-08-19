import sys

sys.stdin = open("_Flatten.txt")

T = 10 # 총 10개의 테스트케이스가 주어짐
for tc in range(1, T +1): # 10번 반복 
    N = int(input()) # 덤프 가능 횟수 넣기 
    numbers = list(map(int, input().split())) # 기둥들 높이를 받음
    for i in range(N): # 덤프 가능 횟수 만큼 반복
        max_num = max(numbers) # 가장 높은 기둥 높이, 예제 경우 처음 옆기둥
        min_num = min(numbers) # 가장 낮은 기둥 높이 
        index_max_num = numbers.index(max_num) # 가장 높은 기둥 높이의 자리(인덱스)숫자 구함 => 예제에서는 9의 자리가 6,7이고 그중 앞에 있는 것이 6임
        index_min_num = numbers.index(min_num) # 가장 낮은 기둥 높이의 자리(인덱스)숫자 구함 => 예제에서는 1의 자리가 3임
        numbers[index_max_num] -= 1 # 가장 높은 기둥자리 인덱스 6 자리에서 한개를 뺌
        numbers[index_min_num] += 1 # 가장 낮은 기둥자리 3에 1을 추가함
    print(f'#{tc} {max(numbers)-min(numbers)}')