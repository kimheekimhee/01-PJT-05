# N명의 사람이 살아
# 사람은 1-N번까지의 번호 (node)
# 두 사람이 서로 아는 관계(edge) 혹은 몇사람 거쳐서 알수있으면 = 무리
# 몇개의 무리?
# test_case = T
# node, edge = map(int,input().split())
# m 개의 줄
# node node 관계 있는 사람들 번호

import sys
sys.stdin = open("_창용마을무리의개수.txt")
T = int(input())
for test_case in range(1,T+1):
    n, e = map(int,input().split())
    graph_list = [[] for _ in range(n+1)]
    visited = [False]*(n+1)
    visited[0] = True
    # print(visited)
    cnt = 0

    for _ in range(e):
        u,v = map(int,input().split())
        graph_list[u].append(v)
        graph_list[v].append(u)
    for i in range(n+1):
        stack = [i]
        if not visited[i]:
            visited[i] = True
            cnt += 1
            while stack:
                cur = stack.pop()
                for adj in graph_list[cur]:
                    if not visited[adj]:
                        visited[adj] = True
                        stack.append(adj)
    result = cnt    
    print(f'#{test_case} {result}')
