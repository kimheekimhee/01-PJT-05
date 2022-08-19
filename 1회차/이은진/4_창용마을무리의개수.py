import sys

sys.stdin = open("_창용마을무리의개수.txt")

for t in range(1, int(input()) + 1):
    node, edge = map(int, input().split())
    
    graph = [[] for _ in range(node + 1)]
    for _ in range(edge):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)

    visit =['x' for _ in range(node + 1)]

    def dfs(start):
        visit[start] = 'o'
        sign = [start]

        while sign:
            now = sign.pop()
            for adj in graph[now]:
                if visit[adj] == 'x':
                    visit[adj] = 'o'
                    sign.append(adj)
    cnt = 0
    for p in range(1, node+1):
        if visit[p] == 'x':
            dfs(p)
            cnt += 1
    print(f'#{t} {cnt}')
