# SWEA 3499. 퍼펙트 셔플

import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    S = list(input().split())

    if len(S) % 2 == 0:
        left = S[:len(S) // 2]
        right = S[len(S) // 2:]
    else:
        left = S[:len(S) // 2 + 1]    # ex) 0, 1, 2, 3
        right = S[len(S) // 2 + 1:]   # ex) 4, 5, 6

    result =  []
    while left or right:
        if left:
            result.append(left.pop(0))
        if right:
            result.append(right.pop(0))
        
    print(f'#{i}', *result)