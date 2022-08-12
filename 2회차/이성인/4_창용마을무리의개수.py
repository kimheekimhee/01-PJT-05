import sys

sys.stdin = open("_창용마을무리의개수.txt") # 이건 연결갯수 문제네요.ㅎㅎ
answer_list = []
T = int(input())
for t in range(T):
    N,M = map(int, input().split())
    visited = []
    town_list = []
    for n in range(N+1):
        visited.append(False)
        town_list.append([])

    for m in range(M):
        v1, v2 = map(int, input().split())
        town_list[v1].append(v2)
        town_list[v2].append(v1)
    stack = []
    cnt = 0
    for i in range(1,N+1):
        check = False
        stack.append(i)
        while stack:
            st = stack.pop()
            if visited[st] == False:
                visited[st] = True
                check = True
                for j in town_list[st]:
                    stack.append(j)
        if check == True:
            cnt += 1
    answer_list.append(cnt)
for ans in range(T):
    print(f"#{ans+1} {answer_list[ans]}") #
