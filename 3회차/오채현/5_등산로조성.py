import sys

sys.stdin = open("_등산로조성.txt")

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    print(matrix)
