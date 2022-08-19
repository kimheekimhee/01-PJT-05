import sys

sys.stdin = open("_등산로조성.txt")
from collections import deque

# 지현식님 코드 참고 작성 코드
# test_case = int(input())
# for test in range(1, test_case + 1):
#     size, depth = list(map(int, input().split()))
#     maps = []
#     highest = 0
#     for i in range(size):
#         line = list(map(int, input().split()))
#         num = max(line)
#         if num > highest:
#             highest = num
#         maps.append(line)
    
#     check =[]
#     for i in range(size):
#         for j in range(size):
#             if maps[i][j] == highest:
#                 check.append([i, j])

#     di = [1, -1, 0, 0]
#     dj = [0, 0, -1, 1]

#     def bfs(a, b):
#         q = deque()
#         q.append((a, b, 1))
#         length = 0
#         while q:
#             i, j, cnt = q.popleft()
#             length = max(length, cnt)
#             for x in range(4):
#                 ni = i + di[x]
#                 nj = j + dj[x]

#                 if ni in range(size) and nj in range(size):
#                     if maps[ni][nj] < maps[i][j]:
#                         q.append((ni, nj, cnt + 1))

#         return length

#     def fix(size, depth):
#         route = []
#         for i in range(size):
#             for j in range(size):
#                 for fix in range(1, depth + 1):
#                     maps[i][j] -= fix
#                     for a, b in check:
#                         route.append(bfs(a, b))
#                     maps[i][j] += fix
#         return max(route)
    
#     print(f'#{test} {fix(size, depth)}')



                


# 구글링 통해 나온 재귀를 활용하는 방법 적용 시도 실패 코드
# test_case = int(input())
# for test in range(1, test_case + 1):
#     size, depth = list(map(int, input().split()))
#     maps = []
#     highest = 0
#     for i in range(size):
#         line = list(map(int, input().split()))
#         num = max(line)
#         if num > highest:
#             highest = num
#         maps.append(line)
    
#     check =[]
#     for i in range(size):
#         for j in range(size):
#             if maps[i][j] == highest:
#                 check.append([i, j])
    
#     di = [1, -1, 0, 0]
#     dj = [0, 0, 1, -1]
    
#     def bfs(a, b, n, bool):
#         q = deque()
#         q.append((a, b, n, bool))
#         length = 0
#         while q:
#             x, y, cnt, cut = q.popleft()
#             if length < cnt:
#                 length = cnt
#             for i in range(4):
#                 ni = x + di[i]
#                 nj = y + dj[i]
#                 if ni in range(size) and nj in range(size):
#                     if maps[ni][nj] < maps[x][y]:
#                         q.append((ni, nj, cnt+1, True))
#                     elif cut == True and (maps[ni][nj] - depth) < maps[x][y]:
#                         before = maps[ni][nj]
#                         maps[ni][nj] = maps[x][y] - 1
#                         result = bfs(ni, nj, cnt+1, False)
#                         maps[ni][nj] = before
#                         if result > length:
#                             length = result

#         return length

#     route = []
#     for i in check:
#         route.append(bfs(i[0], i[1], 1, True))
#     print(route)
