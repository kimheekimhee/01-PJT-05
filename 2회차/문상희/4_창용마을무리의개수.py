import sys

sys.stdin = open("_창용마을무리의개수.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    people, times = list(map(int, input().split()))
    gragh = []
    check = []
    for _ in range(people + 1):
        gragh.append([])
        check.append(0)
    
    for _ in range(times):
        i, j = list(map(int, input().split()))
        gragh[i].append(j)
        gragh[j].append(i)

    def dfs(x):
        stack = [x]
        check[x] = 1
        while stack:
            cur = stack.pop()
            for i in gragh[cur]:
                if check[i] == 0:
                    check[i] = 1
                    stack.append(i)
    cnt = 0
    for i in range(1, people + 1):
        if check[i] == 0:
            cnt += 1
            dfs(i)
    print(f'#{test} {cnt}')