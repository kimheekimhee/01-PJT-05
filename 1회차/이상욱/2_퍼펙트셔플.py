import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for t in range(1, T+1):
    n = int(input())
    card = list(input().split())
    f = []
    b = []
    new = []

    if n%2 != 0:
        for i in range(n//2 + 1):
            f.append(card[i])
        
        for j in range((n//2)+1, n):
            b.append(card[j])
    else:
        for i in range(n//2):
            f.append(card[i])
        for j in range((n//2), n):
            b.append(card[j])

    while f or b:
        if f:
            new.append(f.pop(0))
        if b:
            new.append(b.pop(0))

    print(f'#{t}', *new)