from collections import deque
import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for i in range(1, T+1):
    N = int(input())
    li = list(map(str, input().split()))
    answer = []
    # 012 345
    if N % 2 == 0:
        A = N//2
    # 012 34
    else:
        A = (N//2) + 1
    for j in range(A):
        answer.append(li[j])
        if j + A < N:
            answer.append(li[j+A])
    print(f'#{i}', *answer)