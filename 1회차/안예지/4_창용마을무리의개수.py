import sys

sys.stdin = open("_창용마을무리의개수.txt")

""" 
1 2
2 5
5 1
3 4
4 6

"""
T = int(input())
for t in range(1, T + 1):    
    N, M = map(int, input().split())
    # N, M = 6, 5

    relation = [[] for _ in range(N + 1)]
    # print(relation)

    # 인접리스트 만들기
    for _ in range(M):
        v1, v2 = map(int, input().split())
        relation[v1].append(v2)
        relation[v2].append(v1)
    # print(relation)

    # 방문 리스트 만들기
    visited = [False] * (N + 1)
    merge = 0

    for node in range(1, N + 1):
        
        if visited[node] != True:
            stack = [node]
            visited[node] = True
            
            while len(stack) != 0:
                cur = stack.pop()
                
                for adj in relation[cur]:
                    if visited[adj] != True:
                        visited[adj] = True
                        stack.append(adj)
            merge += 1

    print(f'#{t} {merge}')
    