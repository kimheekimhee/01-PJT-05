import sys

sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())
for t_case in range(1, t + 1):

    n = int(input())
    cards = list(input().split())
    # print(cards)

    half = 0

    if len(cards)%2 == 0:
        half = len(cards)//2
    else:
        half = (len(cards)//2) + 1
    a = [cards[i] for i in range(0, half)]
    b = [cards[i] for i in range(half, len(cards))]
    # print(a, b, sep='\n')
    ab = [a, b]
    # print(ab)
    out = []
    for x in range(len(a)):
        for y in range(len(ab)):
            try:
                out.append(ab[y][x])
            except:
                break
    print(f'#{t_case}', *out, sep=' ')
