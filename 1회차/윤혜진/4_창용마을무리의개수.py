# D4-창용 마을 무리의 개수



# 입력
'''
1. 테스트 케이스 수 T
2. 사람 수 N, 서로를 알고 있는 사람의 관계 수 M
- 1 <= N <= 100
- 0 <= M <= N(N-1) / 2
3. M개의 줄에 서로 알고 있는 두 사람의 번호
- 사람은 1번부터 N번까지 번호가 붙여져 있음
- 같은 관계는 반복해서 주어지지 않음
'''



# 출력
'''
1. #{테스트 케이스} {무리의 개수}
- 몇 사람 거쳐서 아는 관계라면 이러한 사람들 모두 다 묶어서 하나의 무리로 취급
'''



# 코드 1
import sys

sys.stdin = open("input_text/_창용마을무리의개수.txt")

def dfs(node) -> None:
    visited[node] = True   # 시작 노드 방문 체크
    stack = [node]   # 방문했던 노드 순서
    while stack:
        now = stack.pop()   # 현재 위치하고 있는 노드

        # 인접 노드 탐색
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True   # 방문 처리
                stack.append(n)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 사람들 간의 관계 그래프 만들기 (무방향 그래프의 인접 리스트)
    graph = [[] for _ in range(N + 1)]   # 사람 번호: 1번 ~ N번
    for _ in range(M):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    # 관계있는 사람들 무리 찾기
    visited = [False] * (N + 1)
    cnt = 0    
    for p in range(1, N + 1):
        if not visited[p]:
            dfs(p)
            cnt += 1
    
    print(f'#{test_case} {cnt}')



# 실행시간(메모리:64,012 kb, 시간:212 ms)



# 코드 2
import sys

sys.stdin = open("input_text/_창용마을무리의개수.txt")

def dfs(node) -> None:
    visited[node] = True   # 방문 처리

    # 인접 노드 탐색
    for n in graph[node]:
        if not visited[n]:
            dfs(n)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 사람들 간의 관계 그래프 만들기 (무방향 그래프의 인접 리스트)
    graph = [[] for _ in range(N + 1)]   # 사람 번호: 1번 ~ N번
    for _ in range(M):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    # 관계있는 사람들 무리 찾기
    visited = [False] * (N + 1)
    cnt = 0    
    for p in range(1, N + 1):
        if not visited[p]:
            dfs(p)
            cnt += 1
    
    print(f'#{test_case} {cnt}')



# 실행시간(메모리:63,996 kb, 시간:211 ms)



# 코드 3
import sys
from collections import deque

sys.stdin = open("input_text/_창용마을무리의개수.txt")

def bfs(node) -> None:
    visited[node] = True   # 시작 노드 방문 체크
    q = deque([node])   # 방문했던 노드 순서
    while q:
        now = q.pop()   # 현재 위치하고 있는 노드

        # 인접 노드 탐색
        for n in graph[now]:
            if not visited[n]:
                visited[n] = True   # 방문 처리
                q.append(n)


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())

    # 사람들 간의 관계 그래프 만들기 (무방향 그래프의 인접 리스트)
    graph = [[] for _ in range(N + 1)]   # 사람 번호: 1번 ~ N번
    for _ in range(M):
        p1, p2 = map(int, input().split())
        graph[p1].append(p2)
        graph[p2].append(p1)

    # 관계있는 사람들 무리 찾기
    visited = [False] * (N + 1)
    cnt = 0    
    for p in range(1, N + 1):
        if not visited[p]:
            bfs(p)
            cnt += 1
    
    print(f'#{test_case} {cnt}')



# 실행시간(메모리:66,160 kb, 시간:247 ms)