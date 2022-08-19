import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-05\\3회차\\이명학\\_창용마을무리의개수.txt")

T = int(input())

# N 사람의 수, M 서로를 알고 있는 관계 수
N, M = map(int, input().split())
