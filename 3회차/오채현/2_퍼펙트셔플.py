import math
import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(map(str, input().split()))
    m = math.ceil(n/2)
    A = cards[:m]
    B = cards[m:]
    pers = []
    while A or B:
        if A:
            pers.append(A.pop(0))
        if B:
            pers.append(B.pop(0))
    print(f'#{test_case}', *pers)
