import sys

sys.stdin = open("_창용마을무리의개수.txt")

T = int(input())
for t in range(1,T+1):
    # 정점 수, 간선 수
    n, m = map(int,input().split())
    # 카운트 용도
    cnt = 0

    # 인접 리스트 생성
    p = [[] for _ in range(n+1)]
    for i in range(m):
        a, b = map(int,input().split())
        p[a].append(b)
        p[b].append(a)
    
    # 방문 체크용 리스트
    v = [False] * (n+1)
    
    # dfs 함수
    def dfs(start):

        # 시작 번호 스택에 넣고 방문 처리
        stack = [start]
        v[start] = True

        # 스택이 비어있지 않다면 계속 반복
        while stack:
            # 현재 노드 스택에서 꺼내기
            node = stack.pop()

            # 인접 정점 조회
            for adj in p[node]:
                # 해당 정점이 방문하지 않았다면
                if not v[adj]:
                    # 방문처리하고 스택에 넣기
                    v[adj] = True
                    stack.append(adj)

    # 모든 정점 방문 확인
    for j in range(1, n+1):
        # 해당 정점이 방문하지 않았다면 dfs함수 사용
        if v[j] == False:
            dfs(j)
            # 그 후 카운트
            cnt += 1

    print(f'#{t}', cnt)