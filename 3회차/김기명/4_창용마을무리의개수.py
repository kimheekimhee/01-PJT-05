import sys

sys.stdin = open("_창용마을무리의개수.txt")
# N 명 사람있음 서로알거나 거쳐서 알수있는관계면 하나의 무리. 몇개의 무리가있는지 계산하기 .




T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 사람수 N , 관계 수 M

    graph = [[] * M for i in range(N + 1)]

    for i in range(M):
        r1, r2 = map(int, input().split())  #인접 리스트 만들기?
        graph[r1].append(r2)
        graph[r2].append(r1)

    visited = [False] * (N + 1)

    def dfs(start):
        stack = [start]
        visited[start] = True
        while stack:                    # while stack: 을 안넣어서 이상한 결과가 나와서 오래 헤맸음
            cur = stack.pop()
            for adj in graph[cur]:
                if not visited[adj]:
                    visited[adj] = True
                    stack.append(adj)
        
    cnt = 0
    for i in range(1, N + 1):
        if not visited[i]:
            dfs(i)
            cnt += 1
    print(f'#{test_case} {cnt}')
    