# import sys

# sys.stdin = open("_퍼펙트셔플.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    length = int(input())
    base = list(map(str, input().split()))
    half = []
    for _ in range(length // 2):
        x = base.pop()
        half = [x] + half
    
    
    print(f'#{test}', end = ' ')
    for i in range(length // 2):
        print(base[i], end = ' ')
        print(half[i], end = ' ')
    if length % 2 == 0:
        print()
    else:
        print(base[-1])