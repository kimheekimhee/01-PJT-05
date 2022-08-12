# 간선을 입력 받고 그래프 개수 출력하는 문제
T = int(input())

def dfs():
    global d, N, M

    visited = [False] * (N + 1)
    stack = []
    count = 0

    for i in range(1, N + 1):
        if not visited[i]:
            stack.append(i)

            while stack:
                l = stack.pop()

                if not visited[l]:
                    visited[l] = True

                    for j in d[l]:
                        if not visited[j]:
                            stack.append(j)
        
            count += 1

    return count


for i in range(1, T + 1):
    N, M = map(int, input().split())

    d = {j:[] for j in range(1, N + 1)}

    for _ in range(M):
        u, v = map(int, input().split())
        d[u].append(v)
        d[v].append(u)

    ret = dfs()

    print(f"#{i}", ret)