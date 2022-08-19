import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())
    answer = []
    l = 0
    r = (N+1) // 2
    for _ in range(N//2):
        answer.append(card[l])
        answer.append(card[r])
        l, r = l+1, r+1

    if N % 2:
        answer.append(card[N//2])

    print('#{} {}'.format(tc, ' '.join(map(str, answer))))