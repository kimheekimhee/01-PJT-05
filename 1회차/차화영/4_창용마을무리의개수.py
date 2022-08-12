import sys

sys.stdin = open("_창용마을무리의개수.txt")

# 문제 이해는 했으나 코드 구현을 못했습니다.
T = int(input())
for tc in range(1, T+1):
    n, m = map(int, input().split())
    for _ in range(m):
        a, b = map(int, input().split())