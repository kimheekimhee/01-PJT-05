import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for test_case in range(1, T + 1):
    n, m = map(int, input().split())

    graph = [[] for _ in range(n+1)]
    vst = [False] * (n+1)

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    def dfs(st):
        stk = [st]
        vst[st] = True

        while stk:
            cur = stk.pop()
            for adj in graph[cur]:
                if not vst[adj]:
                    vst[adj] = True
                    stk.append(adj)

    cnt = 0

    for i in range(1, n+1):
        if not vst[i]:
            dfs(i)
            cnt += 1
    print(f'#{test_case} {cnt}')
