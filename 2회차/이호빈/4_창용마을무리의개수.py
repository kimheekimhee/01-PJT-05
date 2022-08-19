import sys

sys.stdin = open("_창용마을무리의개수.txt")
##### 1번째 방법
T = int(input())
for tc in range(1, T + 1):
     #n은 정점의 개수, m은 간선의 개수
    n, m = map(int, input().split())
     #인접 리스트를 만들어준다.
    graph = [[] for _ in range(n + 1)]
    #정답을 담을 리스트
    result = 0
    #간선의 개수만큼 돌아주면서
    for _ in range(m):
        #인접리스트에 값을 담아준다.
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    
    #방문을 위한 체크리스트 사람은 1부터 시작하니까 n + 1
    visited = [False] * (n + 1)
    #결과값을 다음 리스트
    cnt = 0
    #모든 노드를 돌아주면서 방문하지 않은 노드들부터 방문해준다.
    for i in range(1, n + 1):
        #방문하지 않은 노드면 queue에 넣어주고 += 1을 해준다.
        if not visited[i]:
            cnt += 1
            queue = [i]
        # queue가 있을때까지
        while queue:
            cur = queue.pop(0)
            for adj in graph[cur]:
                if not visited[adj]:
                    queue.append(adj)
                    visited[adj] = True

    print(f"{tc} {cnt}")

######## 2번째 방법
#dfs 함수를 만들어준다
def dfs(start):
    #스택에 시작값을 넣어주고
    stack = [start]
    #방문했으면 True
    visited[start] = True

    #스택에 값이 있을때까지 돌아주고
    while stack:
        #처음 값들을 pop해주고
        cur = stack.pop(0)

        #인접한 노드를 돌아주면서
        for adj in graph[cur]:
            #방문하지 않으면 방문 처리해 주고 리스트에 추가해준다.
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)


#tc값
T = int(input())
for tc in range(1, T + 1):
    #입력값을 받아주고
    n, m = map(int, input().split())

    #인접 리스트를 만든다.
    graph = [[] for _ in range(n + 1)]

    #방문할 노드를 체크
    visited = [False] * (n + 1)
    for _ in range(m):
        #입력 값 받아준다.
        r1, r2 = map(int, input().split())
        graph[r1].append(r2)
        graph[r2].append(r1)

    #결과값
    cnt = 0
    #graph가 다 돌아야한다.
    for start in range(1, n + 1):
        #방문하지 않으면
        if not visited[start]:
            #dfs를 돌아주고
            dfs(start)
            #결과값을 더해준다.
            cnt += 1

    print(f"{tc} {cnt}")