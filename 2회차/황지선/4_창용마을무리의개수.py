import sys

sys.stdin = open("_창용마을무리의개수.txt")


# 창용 마을에는 N명의 사람이 살고 있다.
# 사람은 편의상 1번부터 N번 사람까지 번호가 붙어져 있다고 가정한다.
# 두 사람은 서로를 알고 있는 관계일 수 있고, 아닐 수 있다.
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면,
# 이러한 사람들을 모두 다 묶어서 하나의 무리라고 한다.
# 창용 마을에 몇 개의 무리가 존재하는지 계산하는 프로그램을 작성하라.


# from pprint import pprint

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for t in range(T):
    # 각 테스트 케이스의 첫 번째 줄에는 각각 창용 마을에 사는 사람의 수와 (점)
    # 서로를 알고 있는 사람의 관계 수를 나타내는 (선)
    # 두 정수 N, M(1 ≤ N ≤ 100, 0 ≤ M ≤ N(N-1)/2) 이 공백 하나로 구분되어 주어진다.
    N, M = map(int, input().split())
    
    graph = [[] for _ in range(N + 1)] # 무방향 인접 그래프 만들기

    for i in range(M):
        # 이후 M개의 줄에 걸쳐서 서로를 알고 있는 두 사람의 번호가 주어진다.
        n1, n2 = map(int, input().split())

        # 그래프에 기록
        graph[n1].append(n2)
        graph[n2].append(n1)

    # pprint(graph)
    # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
    # [[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]    

    count = 0
    visit_list = [False] * (N+1)

    def dfs(house):
        visit_list[house] = True
        stack = [house]

        while stack:
            now = stack.pop()

            for n in graph[now]:
                if not visit_list[n]:
                    visit_list[n] = True
                    stack.append(n)

    for house in range(1, N + 1):
        # 방문하지 않았다면 해당 노드를 시작으로 dfs 돌리고 count += 1
        if not visit_list[house]:
            dfs(house)
            count += 1

    # 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
    # 무리의 개수를 출력한다.
    print(f'#{t+1} {count}')