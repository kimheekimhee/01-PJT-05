# 백준 연결요소의 개수 와 똑같은 문제이다.
import sys

sys.stdin = open("_창용마을무리의개수.txt")

def dfs(start):
    visit[start] = True

    for i in graph[start]:
        if not visit[i]:
            dfs(i)

for test_case in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    # 그래프
    graph = [[] for _ in range(n + 1)]
    # 방문 요소
    visit = [False] * (n + 1)

    # 인접 리스트
    for _ in range(m):
        a, b = map(int, input().split())
        # 서로 연결
        graph[a].append(b)
        graph[b].append(a)
    # 카운트 변수
    cnt = 0
    for i in range(1, n + 1):
        if not visit[i]:
            dfs(i)
            cnt += 1
    print(f"#{test_case} {cnt}")