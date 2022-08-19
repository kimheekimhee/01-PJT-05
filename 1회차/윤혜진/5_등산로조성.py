# 문제-등산로조성



# 입력
'''
1. 테스트 케이스 수 T
2. 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K
- 3 <= N <= 8
- 1 <= K <= 5
- 1 <= 지형의 높이 <= 20
- 가장 높은 봉우리는 최대 5개
- 지형을 깎아 높이를 1보다 작게 만드는 것도 가능
3. N개의 줄에 N x N 크기의 지도 정보
'''



# 출력
'''
1. #{tesr_case} {가장 긴 등산로 길이}
<등산로를 만드는 규칙>
1) 등산로는 가장 높은 봉우리에서 시작해야 함
2) 반드시 높은 지형 -> 낮은 지형으로 가로 또는 세로 방향으로 연결이 되어야 함
    - 높이가 같은 곳은 연결 불가
3) 딱 한 곳을 정해서 최대 K 깊이만큼 지형을 깎을 수 있음
'''



# 코드 1
import sys
import copy
from pprint import pprint

sys.stdin = open("input_text/_등산로조성.txt")

# 가장 높은 봉우리 위치 찾기
def find_peaks(graph, N):
    peaks = []
    max_h = 0   # 가장 높은 봉우리 높이
    for r in range(N):
        for c in range(N):
            if graph[r][c] > max_h:
                max_h = graph[r][c]   # 높이 갱신
                peaks = [(r, c)]   # 봉우리 좌표 초기화
            elif graph[r][c] == max_h:
                peaks.append((r, c))
    
    return peaks


# 등산로 만들기
# 해당 봉우리에서 가장 긴 등산로 길이 반환
def dfs(node) -> int:
    visited = [[False] * N for _ in range(N)]   # 방문 기록 초기화
    start_r, start_c = node
    visited[start_r][start_c] = 1   # 시작 노드 방문 기록
    stack = [node]   # 방문 순서 기록
    max_cnt = 1
    
    while stack:
        r, c = stack.pop()   # 현재 위치하고 있는 좌표

        # 연결 가능한 인접 등산로 탐색
        dr = [0, 0, 1, -1]    # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph) and graph[nr][nc] < graph[r][c]:
                visited[nr][nc] = visited[r][c] + 1
                max_cnt = max(max_cnt, visited[nr][nc])
                stack.append((nr, nc)) 
               
    return max_cnt

    
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) 

    # 지도 그래프 만들기
    graph = [list(map(int, input().split())) for _ in range(N)]
    ori = copy.deepcopy(graph)   # 그래프 원본 복사

    # 공사하지 않은 지도에서 가장 긴 등산로 찾기
    max_road = 0
    peaks = find_peaks(graph, N)   # 가장 높은 봉우리 위치 찾기
    for peak in peaks:
        max_road = max(max_road, dfs(peak))    # 지도에서 가장 긴 등산로 찾기

    # 지도를 순차적으로 순회하면서 각 지형을 최대 K번 깎기
    for r in range(N):
        for c in range(N):
            # 최대 K번 공사함
            for cut in range(1, K + 1):
                graph = copy.deepcopy(ori)   # 그래프 초기화
                graph[r][c] -= cut
            
                # 가장 높은 봉우리 위치 찾기
                peaks = find_peaks(graph, N)   

                # 지도에서 가장 긴 등산로 찾기
                for peak in peaks:
                    max_road = max(max_road, dfs(peak))
    
    print(f'#{test_case} {max_road}')



# 실행결과(실패: 51개 테스트 케이스 중 50개만 통과)



# 코드 2 - 공사 후, graph를 새로 할당해주는 것이 아니라 복구하는 방식으로 코드 작성
import sys
from pprint import pprint

sys.stdin = open("input_text/_등산로조성.txt")

# 가장 높은 봉우리 위치 찾기
def find_peaks(graph, N):
    peaks = []
    max_h = 0   # 가장 높은 봉우리 높이
    for r in range(N):
        for c in range(N):
            if graph[r][c] > max_h:
                max_h = graph[r][c]   # 높이 갱신
                peaks = [(r, c)]   # 봉우리 좌표 초기화
            elif graph[r][c] == max_h:
                peaks.append((r, c))
    
    return peaks


# 해당 봉우리에서 가장 긴 등산로 길이 반환
def dfs(node) -> int:
    visited = [[False] * N for _ in range(N)]   # 방문 기록 초기화
    start_r, start_c = node
    visited[start_r][start_c] = 1   # 시작 노드 방문 기록
    stack = [node]   # 방문 순서 기록
    max_cnt = 1
    
    while stack:
        r, c = stack.pop()   # 현재 위치하고 있는 좌표

        # 연결 가능한 인접 등산로 탐색
        dr = [0, 0, 1, -1]    # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph) and graph[nr][nc] < graph[r][c]:
                visited[nr][nc] = visited[r][c] + 1
                max_cnt = max(max_cnt, visited[nr][nc])
                stack.append((nr, nc)) 
               
    return max_cnt

    
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) 

    # 지도 그래프 만들기
    graph = [list(map(int, input().split())) for _ in range(N)]

    # 공사하지 않은 지도에서 가장 긴 등산로 찾기
    max_road = 0
    peaks = find_peaks(graph, N)   # 가장 높은 봉우리 위치 찾기
    for peak in peaks:
        max_road = max(max_road, dfs(peak))    # 지도에서 가장 긴 등산로 찾기

    # 지도를 순차적으로 순회하면서 각 지형을 최대 K번 깎기
    for r in range(N):
        for c in range(N):
            # 최대 K번 공사함
            for cut in range(1, K + 1):
                graph[r][c] -= cut
            
                # 가장 높은 봉우리 위치 찾기
                peaks = find_peaks(graph, N)   

                # 지도에서 가장 긴 등산로 찾기
                for peak in peaks:
                    max_road = max(max_road, dfs(peak))
                
                 # 그래프 복구
                graph[r][c] += cut

    print(f'#{test_case} {max_road}')



# 실행결과(실패: 51개 테스트 케이스 중 50개만 통과)



# 코드 3 - 지도에서 가장 높은 봉우리 위치(즉, 스타트 위치)는 변하면 안됨!!!!!
import sys
from pprint import pprint

sys.stdin = open("input_text/_등산로조성.txt")

# 가장 높은 봉우리 위치 찾기
def find_peaks(graph, N):
    peaks = []
    max_h = 0   # 가장 높은 봉우리 높이
    for r in range(N):
        for c in range(N):
            if graph[r][c] > max_h:
                max_h = graph[r][c]   # 높이 갱신
                peaks = [(r, c)]   # 봉우리 좌표 초기화
            elif graph[r][c] == max_h:
                peaks.append((r, c))
    
    return peaks


# 해당 봉우리에서 가장 긴 등산로 길이 반환
def dfs(node) -> int:
    visited = [[False] * N for _ in range(N)]   # 방문 기록 초기화
    start_r, start_c = node
    visited[start_r][start_c] = 1   # 시작 노드 방문 기록
    stack = [node]   # 방문 순서 기록
    max_cnt = 1
    
    while stack:
        r, c = stack.pop()   # 현재 위치하고 있는 좌표

        # 연결 가능한 인접 등산로 탐색
        dr = [0, 0, 1, -1]    # 동서남북
        dc = [1, -1, 0, 0]
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < len(graph) and 0 <= nc < len(graph) and graph[nr][nc] < graph[r][c]:
                visited[nr][nc] = visited[r][c] + 1
                max_cnt = max(max_cnt, visited[nr][nc])
                stack.append((nr, nc)) 
               
    return max_cnt

    
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) 

    # 지도 그래프 만들기
    graph = [list(map(int, input().split())) for _ in range(N)]
   
    # 가장 높은 봉우리 위치 찾기
    peaks = find_peaks(graph, N)   

    # 지도를 순차적으로 순회하면서 각 지형을 최대 K번 깎기
    max_road = 0
    for r in range(N):
        for c in range(N):
            # 최대 K번 공사함
            for cut in range(0, K + 1):
                graph[r][c] -= cut

                # 지도에서 가장 긴 등산로 찾기
                for peak in peaks:
                    max_road = max(max_road, dfs(peak))
                
                 # 그래프 복구
                graph[r][c] += cut

    print(f'#{test_case} {max_road}')



# 실행결과(메모리:63,272 kb, 시간:768 ms)



# 코드 4 - 코드 3 풀이에서, 스택 대신 재귀를 이용해서 dfs 구현
import sys
from pprint import pprint

sys.stdin = open("input_text/_등산로조성.txt")

# 가장 높은 봉우리 위치 찾기
def find_peaks(graph, N):
    peaks = []
    max_h = 0   # 가장 높은 봉우리 높이
    for r in range(N):
        for c in range(N):
            if graph[r][c] > max_h:
                max_h = graph[r][c]   # 높이 갱신
                peaks = [(r, c)]   # 봉우리 좌표 초기화
            elif graph[r][c] == max_h:
                peaks.append((r, c))
    
    return peaks


# 해당 봉우리에서 가장 긴 등산로 길이 찾아 갱신
def dfs(node, cnt) -> None:
    global max_road
    
    # 등산로 길이 갱신
    max_road = max(max_road, cnt)

    # 연결 가능한 인접 등산로 탐색
    dr = [0, 0, 1, -1]    # 동서남북
    dc = [1, -1, 0, 0]
    for i in range(4):
        nr = node[0] + dr[i]
        nc = node[1] + dc[i]
        if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] < graph[node[0]][node[1]]:
            dfs((nr, nc), cnt + 1)

    
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) 

    # 지도 그래프 만들기
    graph = [list(map(int, input().split())) for _ in range(N)]
   
    # 가장 높은 봉우리 위치 찾기
    peaks = find_peaks(graph, N)   

    # 지도를 순차적으로 순회하면서 각 지형을 최대 K번 깎기
    max_road = 0
    for r in range(N):
        for c in range(N):
            # 최대 K번 공사함
            for cut in range(0, K + 1):
                graph[r][c] -= cut

                # 지도에서 가장 긴 등산로 찾기
                for peak in peaks:
                    dfs(peak, 1)
                
                 # 그래프 복구
                graph[r][c] += cut

    print(f'#{test_case} {max_road}')



# 실행결과(메모리:71,448 kb, 시간:1,028 ms)



# 코드 5 - bfs로 탐색
import sys
from collections import deque
from pprint import pprint

sys.stdin = open("input_text/_등산로조성.txt")

# 가장 높은 봉우리 위치 찾기
def find_peaks(graph, N):
    peaks = []
    max_h = 0   # 가장 높은 봉우리 높이
    for r in range(N):
        for c in range(N):
            if graph[r][c] > max_h:
                max_h = graph[r][c]   # 높이 갱신
                peaks = [(r, c)]   # 봉우리 좌표 초기화
            elif graph[r][c] == max_h:
                peaks.append((r, c))
    
    return peaks


# 해당 봉우리에서 가장 긴 등산로 길이 반환
def bfs(r, c) -> int:
    q = deque([(r, c)])   # 방문 순서 기록
    max_cnt = 1
    cnt = 0
    
    while q:
        for _ in range(len(q)):
            r, c = q.popleft()   # 현재 위치하고 있는 좌표

            # 연결 가능한 인접 등산로 탐색
            dr = [0, 0, 1, -1]    # 동서남북
            dc = [1, -1, 0, 0]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N and graph[nr][nc] < graph[r][c]:
                    q.append((nr, nc)) 
        cnt += 1
               
    return max(max_cnt, cnt)

    
T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split()) 

    # 지도 그래프 만들기
    graph = [list(map(int, input().split())) for _ in range(N)]
   
    # 가장 높은 봉우리 위치 찾기
    peaks = find_peaks(graph, N)   

    # 지도를 순차적으로 순회하면서 각 지형을 최대 K번 깎기
    max_road = 0
    for r in range(N):
        for c in range(N):
            # 최대 K번 공사함
            for cut in range(0, K + 1):
                graph[r][c] -= cut

                # 지도에서 가장 긴 등산로 찾기
                for peak in peaks:
                    max_road = max(max_road, bfs(peak[0], peak[1]))
                
                 # 그래프 복구
                graph[r][c] += cut

    print(f'#{test_case} {max_road}')



# 실행결과(메모리:68,940 kb, 시간:601 ms)