import sys

sys.stdin = open("_창용마을무리의개수.txt")




T = int(input())

for tc in range(1,T+1):
    N,M = map(int,input().split())
    adj_list =[[] for _ in range(N+1)]
    visited = [0] * (N + 1)
    ans = 0

    for i in range(M):
        a,b = map(int,input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    for node in range(1,N+1):
        if not visited[node]:
            visited[node] = 1
            ans += 1
            stack = [node]
            while stack:
                now = stack.pop()
                for nxt in adj_list[now]:
                    if not visited[nxt]:
                        visited[nxt] = 1
                        stack.append(nxt)

    print('#{} {}' . format(tc,ans))

    

