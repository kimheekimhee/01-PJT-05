import sys

sys.stdin = open("_창용마을무리의개수.txt")

# 1~n번 사람까지 번호가 붙어져있음
# 두 사람은 서로를 알고 있는 관계일 수 있고 아닐 수 있음
# 두 사람이 서로 아는 관계이거나 몇 사람을 거쳐서 알 수 있는 관계라면, 하나의 무리임
# 몇개의 무리가 존재하는지? 
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    list1 = []
    for i in range(n+1):
        list1.append([]) # 리스트 안애 7개 이중 리스트 생성(안에 리스트는 빈 리스트)
    
    visited = [0] * (n+1) # 0이 7개 들어간 방문기록용 리스트 생성
    ans = 0

    for j in range(m): # 
        a, b = map(int, input().split()) # 관계수 입력 시작 1,2
        list1[a].append(b) # 이중 리스트 중 밖의 리스트 1자리에 2를 넣음
        list1[b].append(a) # 이중 리스트 중 밖의 리스트 2자리에 1을 넣음

    for node in range(1, n+1):
        if not visited[node]:
            visited[node] = 1
            ans += 1
            stack = [node]
            while stack:
                now = stack.pop()
                for nxt in list1[now]:
                    if not visited[nxt]:
                        visited[nxt] = 1
                        stack.append(nxt)
    print(f'#{_+1} {ans}')
        
        

