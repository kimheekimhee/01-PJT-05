import sys
from pprint import pprint

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())

#각 무리를 탐색하는 dfs 탐색 정의
def dfs(start):
    stack = [start]
    visited[start] = 1

    while stack:
        now = stack.pop()
        for item in adjacency_list[now]:
            if visited[item] == 0:
                visited[item] = 1
                stack.append(item)

for _ in range(T):
    node, edge = map(int, input().split())

    #사람들 간의 관계를 나타내는 adjacency_list 생성
    adjacency_list = [[] for i in range(node + 1)]
    for i in range(edge):
        u, v = map(int, input().split())
        adjacency_list[u].append(v)
        adjacency_list[v].append(u)

    #dfs를 활용하여 무리의 갯수 count
    visited = [0] * (node + 1)

    cnt = 0
    for i in range(node + 1):
        if visited[i] == 0:
            dfs(i)
            cnt += 1
    
    print(f'#{_ + 1}', cnt - 1)