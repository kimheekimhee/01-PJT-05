import sys

sys.stdin = open("_창용마을무리의개수.txt")

def DFS(i, graph_list, visited_list, component_list) :
    stack = list()
    component = list()

    stack.append(i)
    while stack :
        p = stack.pop()
        if not visited_list[p] :
            visited_list[p] = True
            component.append(p)
        for n in graph_list[p] :
            if not visited_list[n] :
                stack.append(n)
    component_list.append(component)

T = int(input())
for test_case in range(1, T+1) :
    V, E = map(int, input().split())
    graph = [[] for _ in range(V+1)]
    visited = [False for _ in range(V+1)]
    connected_component = []

    for _ in range(E) :
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)

    for v in range(1, V+1) :
        if not visited[v] :
            DFS(v, graph, visited, connected_component)
    
    print(f'#{test_case} {len(connected_component)}')