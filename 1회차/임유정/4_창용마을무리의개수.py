import sys

sys.stdin = open("_창용마을무리의개수.txt")

for tc in range(1, 1 + int(input())):
    N, M = map(int, input().split())

    for _ in range(M):
        a, b = map(int, input().split())
        adj[a].append(b)
        adj[b].append(a)