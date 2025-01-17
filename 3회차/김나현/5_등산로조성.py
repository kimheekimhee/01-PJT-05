import sys

sys.stdin = open("_등산로조성.txt")

# DFS
# N, K
# K 가 1인 경우
# 1. 제일 큰 숫자 찾기
# 2. 제일 큰 숫자에서 이동하는데
#       그 숫자를 기준으로 상,하,좌,우 델타 탐색
#       조건: 상하좌우가 현재 위치보다 크고, K가 0일 경우 종료
#       현재 위치의 숫자보다 작은 숫자로 이동

#       * 만약 이동하는 곳의 숫자가 현재위치의 숫자와 같으면 -1하고 K--
#           이동하는 곳의 숫자 - K이 현재 위치의 숫자보다 작으면 -K하고 K = 0 변경 후 이동시킨다
#       이동시킬때마다 cnt++
#       만약 K가 0이고 막혀있다면 거기서 중단후 등산로 길이 저장
# 3. 배열 끝까지 도달할때까지 2번을 반복
# 4. 가장 긴 경로 길이(cnt) 출력

T = int(input())
N, K = map(int, input().split())
map_ = [list(map(int, input().split())) for _ in range(N)]

# 제일 큰 숫자 찾기