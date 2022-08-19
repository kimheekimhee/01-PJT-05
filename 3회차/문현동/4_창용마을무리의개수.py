import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    
    edges = []
    visited = []
    adjacent_list = []
    
    for _ in range(M):
        edges.append([*map(int, input().split())])
    
    for _ in range(N + 1):
        adjacent_list.append([])
    
    for i in edges:
        adjacent_list[i[0]].append(i[1])
        adjacent_list[i[1]].append(i[0])
    
    for _ in range(N + 1):
        visited.append(False)
    
    stack = []
    cnt = 0
    
    for j in range(1, N + 1): # 각 무리의 시작점 j
        if not visited[j]:
            # 방문되지 않는다.
            # >>> 이미 방문처리 되어 있다.
            # >>> 예전에 연결되어진 다른 점에 의해 검색되어졌다.
            # >>> 그 다른 점과 지금의 j 는 서로 연결된 하나의 무리에 속해있다.
            # >>> 같은 무리 이므로 cnt += 1 되지 않는다.
            stack = [j]
            while stack:
                visited[j] = True
                current = stack.pop(0)
                for k in adjacent_list[current]:
                    if not visited[k]:
                        visited[k] = True
                        stack.append(k)
            cnt += 1
    
    print(f"#{test_case} {cnt}")