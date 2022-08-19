import sys

sys.stdin = open("_창용마을무리의개수.txt")


# for tc in range(1, 1 +int(input())):
#     n, m = map(int, input().split())
#     # print(n, m) 
#     # 6 5
#     # 1 2
#     adj = {x + 1: [] for x in range(n)}
#     # print(adj)
#     # {1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
#     # {1: []}
#     for _ in range(m):
#         a, b = map(int, input().split())
#         adj[a].append(b)
#         adj[b].append(a)
#         # print(adj[a])
#         # [2]
#         # [1, 5]
#         # [2, 1]
#         # [4]   
#         # [3, 6]
#         # [2]   
#         # [1, 5]
#         # [2, 1]
#         # [4]
#         # [3, 6]
#         # [2, 1, 4]
#         # [1, 5, 4]
#         # [1, 5, 4, 3]
#         # print(adj[b])
#         # [1]
#         # [2]   
#         # [2, 5]
#         # [3]   
#         # [4]   
#         # [1]   
#         # [2]   
#         # [2, 5]
#         # [3]
#         # [4]
#         # [3, 6, 5]
#         # [3, 6, 5, 2]
#         # [4, 2]
#         visited = [0] * (n + 1)
#         #print(visited)   [0, 0, 0, 0, 0, 0, 0]
#         visited[0] = 1
#         #print(visited[0])  1
#         q = deque()
#         #print(q) # deque([])
#         count = 0

#         for i in range(1, n+1):
#             if visited[i] == 0:
#                 count += 1
#                 q.append(i)
#                 visited[i] == 1

#         while q:
#             c = q.popleft()
#             for neighbor in adj[c]:
#                 if visited[neighbor] == 0:
#                     q.append(neighbor)
#                     visited[neighbor] = 1

# print('#{} {}'.format(tc, count))







def bfs(i,j):
    while len(temp) != 0:
        ni,nj = temp.pop(0)
 
        for qq in range(1,n+1):
            if board[ni][qq] == 1:
                board[ni][qq] = 0
                board[qq][ni] = 0
                visited[qq] = 1
                visited[ni] = 1
                temp.append([ni,qq])
 
            if board[nj][qq] == 1:
                board[nj][qq] = 0
                board[qq][nj] = 0
                visited[qq] = 1
                visited[nj] = 1
                temp.append([nj,qq])
 
    return
 
# tc 개수
T = int(input())
 
for tc in range(1,1+T):
    # 주민 수, 관계 수
    n,m = map(int,input().split())
 
    # 관계
    items = [list(map(int,input().split())) for _ in range(m)]
 
    # 관계들 저장해서 for문 돌지 않기 위함
    board = [[0]*(n+1) for _ in range(n+1)]
 
    # 관계가 나오지 않은 곳을 찾기 위해
    visited = [1]+[0]*n
 
    # 무리의 수
    cnt = 0
 
    # 관계가 확인된 곳 저장
    for q in items:
        board[q[0]][q[1]] = 1
        board[q[1]][q[0]] = 1
 
    for w in items:
        # 관계가 확인된 곳이면
        if board[w[0]][w[1]] == 1:
            
            # 무리의 수 + 1 및 board 초기화, visited 변경
            cnt += 1
            temp = [[w[0],w[1]]]
            board[w[0]][w[1]] = 0
            board[w[1]][w[0]] = 0
            visited[w[0]] = 1
            visited[w[1]] = 1
            bfs(w[0],w[1])
 
    # 무리의 숫자 + 관계가 나오지 않은 곳들의 수(사람 하나가 하나의 무리)
    res = cnt + visited.count(0)
 
    print('#{} {}'.format(tc,res))