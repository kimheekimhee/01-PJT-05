import sys, copy

sys.stdin = open("_등산로조성.txt")


T = int(input())

for t in range(T):

    N, K = map(int, input().split())

    S_graph = [list(map(int, input().split())) for _ in range(N)]

    size = 1


    def dfs(x, y,graph):
        if x <= -1 or x >= N or y <= -1 or y >= N:  # 경계조건
            return False

        cnt = 0
        global size

        if graph[x][y] != -10000 :  # 그래프 요소가 1이면 0으로 바꿔준다

            if graph[x][y] == max(map(max, graph)):

                size_list.append(size)
                size = 1
                return True


            if x != N - 1:

                if graph[x][y] < graph[x + 1][y]:
                    size += 1
                    cnt += 1
                    dfs(x + 1, y,graph)

            if x != 0:
                if graph[x][y] < graph[x - 1][y]:
                    size += 1
                    cnt += 1
                    dfs(x - 1, y,graph)

            if y != N - 1:
                if graph[x][y] < graph[x][y + 1]:
                    size += 1
                    cnt += 1
                    dfs(x, y + 1,graph)

            if y != 0:
                if graph[x][y] < graph[x][y - 1]:
                    size += 1
                    cnt += 1
                    dfs(x, y - 1,graph)

            if cnt == 0  :
                size_list.append(size)
                size = 1

            return True  # 1을 0으로 바꿨으면 True를 반환

        return False  # 바꾸지 않았따면 False를 반환


    size_list = []
    S_graph_list = []
    S_graph_input=copy.deepcopy(S_graph)


    # for i in range(N):
    #     for j in range(N):
    #         S_graph_input[i][j] = S_graph[i][j] - K
    #         ans = copy.deepcopy(S_graph_input)
    #         S_graph_list.append(ans)
    #         S_graph_input[i][j] = S_graph[i][j]
    # for k in range(N**2):
    #     for i in range(N):
    #         for j in range(N):
    #             check_min = min(map(min, S_graph_list[k]))
    #             if S_graph_list[k][i][j] == check_min:
    #                 dfs(i,j,S_graph_list[k])

    for i in range(N):
        for j in range(N):

            dfs(i,j,S_graph)
    print(f'#{t+1} {max(size_list)}')






