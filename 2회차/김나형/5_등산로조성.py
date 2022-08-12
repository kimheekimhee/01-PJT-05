import sys

sys.stdin = open("_등산로조성.txt")

T = int(input())
for tc in range(1, T + 1):
    N, K  = map(int, input().split())

    load = [list(map(int, input().split())) for _ in range(N)]
    print(load)