import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input()) # 테스트케이스 개수

def dfs():
    print()
for test_case in range(T):
    N, M = map(int, input().split()) # N:사는 사람 수,M:서로알고있는 관계 수
    relation = [[0] * (N+1) for _ in range(N+1)]
    relation_list = [[0] for _ in range(N+1)]
    result = 0

    for _ in range(M):
        u, v = map(int, input().split())
        relation_list[u].append(v)
        relation_list[v].append(u)
    
    visited = [False] * (N+1)
    stack_list = []