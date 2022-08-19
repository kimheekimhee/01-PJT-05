import sys
from collections import defaultdict
from collections import deque

sys.stdin = open("_창용마을무리의개수.txt")

def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited

T = int(input())

for test_case in range(1,T+1):
    N,M= map(int,input().split())
    all = []
    C_cnt = 0
    graph= defaultdict(list)

    for i in range(1, N + 1):
        all.append(i)

    for _ in range(M):
        k, v = map(int, sys.stdin.readline().split())
        graph[k].append(v)
        graph[v].append(k)

    while True:
        if len(all) == 0:
            break
        else:
            result = dfs(graph, all[0])

            C_cnt += 1

        for i in result:
            all.remove(i)

    print(f'#{test_case} {C_cnt}')