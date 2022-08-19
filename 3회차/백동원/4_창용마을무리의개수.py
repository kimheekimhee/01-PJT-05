import sys

sys.stdin = open("_창용마을무리의개수.txt")
T = int(input())
for _ in range(1, T +1):
    N, M = map(int, input().split())
    matrix = [[] for i in range(N + 1)]
    check = [False] * (N + 1)
    for a in range(M):
        x, y = map(int, input().split())
        matrix[x].append(y)
        matrix[y].append(x)
    stack = []
    cnt = 0
    for c in range(1, N + 1):
        if check[c] == False:
            cnt += 1
            stack.append(c)
            while len(stack) != 0:
                cur = stack.pop()
                check[cur] = True
                for b in matrix[cur]:
                    if check[b] == False:
                        stack.append(b)
    print(f'#{_} {cnt}')