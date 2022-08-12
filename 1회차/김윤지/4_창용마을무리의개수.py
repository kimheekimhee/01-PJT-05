import sys

sys.stdin = open("_창용마을무리의개수.txt")

t = int(input())

for tc in range(1,t+1):
    n, m = map(int,input().split())
    people = [[] for _ in range(n+1)]
    visited = [False] * (n + 1)

    for i in range(m):
        x, y = map(int,input().split())
        people[x].append(y)
        people[y].append(x)
    #print(people) # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]

    stack = []
    stack.append((n, 0))
    visited[n] = True
    #print(stack)
    #그다음부터 못풀겠어요ㅠㅠ
