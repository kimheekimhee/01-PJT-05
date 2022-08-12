import sys
sys.stdin = open("_등산로조성.txt")

T = int(input())
delta = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (0, -1), (-1, 1)]

for i in range(1, T + 1):
    N, K = map(int, input().split())
    graph = []
    for i in range(N):
        graph.append(list(map(int, input().split())))
    cnt = 0
    print(max(max(graph)))

