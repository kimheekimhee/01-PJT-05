# import sys

# sys.stdin = open("_창용마을무리의개수.txt")

# 좀 더 어려운 DFS 문제를 예상하고 잔뜩 긴장해 있었는데 다행히 기본 DFS에 조금 추가된 문제였습니다.
# DFS를 활용하면 출발 노드와 연결된 것들은 방문표시가 되므로, 모든 노드를 DFS를 돌려 False가 전부 다 사라질 때까지 카운트 해서 풀었습니다.
# 함수 선언을 하지 않고 for문 안에 그대로 집어 넣거나, 함수를 위쪽에 만들었어야 했는데 중간에 해버렸습니다.
# 이번에는 다행히 오류가 나지 않았지만 다음부터는 함수를 아예 위쪽에 선언을 하거나 아니면 그냥 for문 안에 그대로 코드를 짜는 식으로 하겠습니다.

T = int(input())
for test_case in range(1, T+1):
    # N, M을 입력받음
    N, M = map(int, input().split())
    

    # 인접 리스트 생성용 빈 리스트
    graph_ = [[] for _ in range(N+1)]

    # 인접 리스트 생성
    for _ in range(M):
        a, b = map(int, input().split())
        graph_[a].append(b)
        graph_[b].append(a)


    # 방문 횟수를 세기 위한 변수 설정    
    cnt = 0

    # 방문 확인용 빈 리스트
    # 노드가 1~N까지 이므로 매칭을 쉽게 하기 위해 N+1개를 선언
    visited = [False] * (N + 1)

    # dfs 선언
    def dfs(start):
        stack = [start]
        visited[start] = True

        while stack:
            cur = stack.pop()

            for adj in graph_[cur]:
                if not visited[adj]:
                    stack.append(adj)
                    visited[adj] = True

    # 모든 노드에 대해서 방문하지 않았을 경우 해당 노드를 이용해 dfs 시행
    # visited[0]은 편의상 생성한 것이므로 범위는 1 ~ N까지
    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            # 시행할 때마다 카운트를 셈
            cnt += 1
        else:
            continue

    print(f'#{test_case} {cnt}')