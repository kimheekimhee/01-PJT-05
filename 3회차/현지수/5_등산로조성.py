import sys

sys.stdin = open("_등산로조성.txt")

t = int(input())
for test_case in range(1, t + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]

    # 4방향 델타탐색
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    # 이게몬가요...