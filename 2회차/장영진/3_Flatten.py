# SWEA 1208. Flatten
# 매번 덤프시 최솟값+1, 최댓값-1
import sys

sys.stdin = open("_Flatten.txt")

for i in range(1, 11):
    dump = int(input()) # 덤프 횟수
    arr = list(map(int, input().split()))

    while dump: # 덤프 횟수만큼 반복
        max_arr = max(arr) # 최대값
        min_arr = min(arr) # 최소값
        max_idx = arr.index(max_arr) # 최대값 인덱스
        min_idx = arr.index(min_arr) # 최소값 인덱스
        arr[max_idx] -= 1 # 최대값 -1
        arr[min_idx] += 1 # 최소값 +1

        dump -= 1 # 덤프 횟수 차감
    print(f'#{i} {max(arr) - min(arr)}')