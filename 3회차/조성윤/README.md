## 후기 작성
마지막 알고리즘 수업이라니 아쉽다...
### 반반
문자열의 각 문자의 count가 전부 2면 조건을 만족한다.
### 모음이 보이지 않는 사람
그냥 replace 5번... 파이썬 갓갓
### 퍼펙트 셔플
카드 수가 홀수일 때와 짝수일 때를 나눠서 풀었다. 
슬라이싱을 통해 카드 덱을 반으로 나눠서 순서대로 추가해줬다.
### Flatten
리스트의 최댓값을 1 빼고 최솟값을 1 더한다. 
이걸 주어진 덤프 횟수만큼 반복한다.
### 창용 마을 무리의 개수
[백준 11724 연결 요소의 개수](https://www.acmicpc.net/problem/11724)와 동일한 문제였다.
### 등산로 조성
스택을 사용한 반복문으로 풀려고 시도했으나
visit 백트래킹 과정에 막혀서 결국 익숙하지도 않은 재귀를 시도해야만 했다.
```python
def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    global max_length
    visited[r][c] = 1
    for dr, dc in delta :
        .
        .
        if mountain[nr][nc] < mountain[r][c] : # 다음 위치의 원래 높이가 기존 위치의 높이보다 낮음
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
        .
        .
        .
    max_length = max(max_length, length) # 길이 갱신
    visited[r][c] = 0

T = int(input())
for test_case in range(1, T+1) :
    .
    .
    .
    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                DFS_construction(i, j, 1, 1) # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    .            
    .            
```
처음엔 이렇게 함수의 처음과 끝부분에서 visit 백트래킹을 시도했고 정답인 줄 알았는데 아니었다.
```python
def DFS_construction(r, c, limit, length) : # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
    .
    .
    .
            visited[nr][nc] = 1 # 방문
            DFS_construction(nr, nc, limit, length+1) # 다음 위치 좌표 및 높이, 공사 안 함, 길이 증가
            visited[nr][nc] = 0 # 끝자락에 도달했으면 역순으로 되돌아가면서 방문 해제
       .
       .
       .
                if mountain[nr][nc] < mountain[r][c] : # 깎은 높이가 기존 높이보다 낮아지면
                    visited[nr][nc] = 1 # 방문
                    DFS_construction(nr, nc, limit-1, length+1) # 다음 위치 좌표 및 높이, 공사함, 길이 증가   
                    visited[nr][nc] = 0 # 끝자락에 도달했으면 역순으로 되돌아가면서 방문 해제
                
                .
                .
T = int(input())
for test_case in range(1, T+1) :
    .
    .
    .
    for i in range(N) :
        for j in range(N) :
            if mountain[i][j] == high_len :           
                visited[i][j] = 1 # 맨 처음 위치 방문
                DFS_construction(i, j, 1, 1) # 현재 위치 좌표, 공사 가능 횟수, 현재 길이
                visited[i][j] = 0 # 모든 호출이 끝나고 마지막으로 처음 위치 방문 해제
    .
    .
```
이렇게 수정했더니 정답이 나오긴 했는데 아직 잘 모르겠다...
