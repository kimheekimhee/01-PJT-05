import sys
sys.stdin = open("_창용마을무리의개수.txt")

def dfs(person):
    visited[person] = 1
    for i in graph[person]:
        if not visited[i]:
            dfs(i)

T = int(input())
#실습에서 나왔던 문제랑 같은 문제.
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    cnt = 0

    for _ in range(m):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    visited = [0] * (n + 1)

    for i in range(1, n + 1):
        if not visited[i]:
            if not graph[i]:
                cnt += 1
                visited[i] = 1
            else:
                dfs(i)
                cnt += 1
    
    print(f'#{test_case} {cnt}')