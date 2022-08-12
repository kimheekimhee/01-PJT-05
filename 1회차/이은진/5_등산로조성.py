import sys

sys.stdin = open("_등산로조성.txt")

for t in range(1, int(input())):
    m, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(m)]
    