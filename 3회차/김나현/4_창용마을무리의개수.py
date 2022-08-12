import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N + 1)]
    visited = [False] * (N + 1)
    visited[0] = True
    stack = []
    for _ in range(M):
        person1, person2 = map(int, input().split())
        graph[person1].append(person2)
        graph[person2].append(person1)   
    cnt = 0
    while visited.count(True) != N + 1:
        j = visited.index(False)
        stack.append(graph[j])
        visited[j] = True
        while stack:
            cur = stack.pop()
            for adj_persons in cur:
                if not visited[adj_persons]:
                    visited[adj_persons] = True
                    stack.append(graph[adj_persons])
        cnt += 1
    print(f'#{test_case} {cnt}')