import sys

sys.stdin = open("_창용마을무리의개수.txt")

# T = int(input())
# for tc in range(1, T + 1):
#     #n은 정점의 개수, m은 간선의 개수
#     n, m = map(int, input().split())
#     #인접 리스트를 만들어준다.
#     graph = [[] for _ in range(n + 1)]
#     #정답을 담을 리스트
#     result = 0
#     #간선의 개수만큼 돌아주면서
#     for _ in range(m):
#         #인접리스트에 값을 담아준다.
#         n1, n2 = map(int, input().split())
#         graph[n1].append(n2)
#         graph[n2].append(n1)
    
#     #방문을 위한 체크리스트 사람은 1부터 시작하니까 n + 1
#     visited = [False] * (n + 1)
#     #결과값을 다음 리스트
#     cnt = 0
#     #모든 노드를 돌아주면서 방문하지 않은 노드들부터 방문해준다.
#     for i in range(1, n + 1):
#         #방문하지 않은 노드면 queue에 넣어주고 += 1을 해준다.
#         if not visited[i]:
#             cnt += 1
#             queue = [i]
#         # queue가 있을때까지
#         while queue:
#             cur = queue.pop(0)
#             for adj in graph[cur]:
#                 if not visited[adj]:
#                     queue.append(adj)
#                     visited[adj] = True

#     print(f"{tc} {cnt}")

def dfs(start):
    stack = [start]
    visited[start] = True

    while stack:
        cur = stack.pop(0)

        for adj in graph[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)



T = int(input())
for tc in range(1, T + 1):
    n, m = map(int, input().split())

    #인접 리스트를 만든다.
    graph = [[] for _ in range(n + 1)]

    #방문할 노드를 체크
    visited = [False] * (n + 1)
    for _ in range(m):
        #입력 값 받아준다.
        r1, r2 = map(int, input().split())
        graph[r1].append(r2)
        graph[r2].append(r1)

    #결과값
    cnt = 0
    for start in range(1, n + 1):
        if not visited[start]:
            dfs(start)
            cnt += 1

    print(f"{tc} {cnt}")