import sys

sys.stdin = open("_창용마을무리의개수.txt")

t = int(input())
for t_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    # print(graph)
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    # print(graph)
    visit = [False] * (n + 1)
    # print(visit)
    moori = 0

    for i in range(1, n + 1):
        if visit[i]:
                continue
        else:
            c_stack =[i]
            visit[i] = True

            while c_stack:
                c = c_stack.pop()
                for adj in graph[c]:
                    if not visit[adj]:
                        visit[adj] = True
                        c_stack.append(adj)
            moori += 1
    print(f'#{t_case} {moori}')