from inspect import stack
import sys

sys.stdin = open("_창용마을무리의개수.txt")
t = int(input())
total = 0
next = [False]*n
for _ in range(1, t+1):
    n,m =map(int, input().split())
    po = [[] for _ in range(n)]
    for i in range(m):
        v1, v2 = map(int, input().split())
        po[v1].append(v2)
        po[v2].append(v1)
def dfs(nxt):
    stack = [nxt]
    next[nxt] = True

    while stack:
        cur =stack.pop()
        for p in po[cur]:
            if not next[nxt]:
                next[nxt] = True
                stack.append(p)
    