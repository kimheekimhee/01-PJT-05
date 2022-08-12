import sys

sys.stdin = open("_창용마을무리의개수.txt")

N, M = list(map(int, input().split()))
# 방문하지 않은 곳들
visited = [False] * (N + 1)

for adj_number in adj_graph():
    stack = []
    stack.append[adj_number]
    visited = True # 방문했으면 True로 변환