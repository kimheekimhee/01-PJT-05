import sys

sys.stdin = open("_퍼펙트셔플.txt")

odd = []
for _ in range(500):
    if _ % 2 != 0:
        odd.append(_)
# print(odd)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    name = list(input().split())
    n = N // 2
    if N % 2 == 0:
        pass
    else:
        n = n + 1

    name_a = name[:n]
    name_b = name[n:]
    # print(name_a)
    # print(name_b)
    
    while len(name_b) != 0:
        for i in odd:
            name_a.insert(i, name_b.pop(0))
            
            if len(name_a) == N:
                break
    print(f'#{tc}', end=' ')
    print(*name_a)