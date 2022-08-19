import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    card = list(input().split())

    result = []
    if len(card)%2 == 0: # 카드 수가 짝수일 경우
        start = card[:(len(card)//2)]
        end = card[len(card)//2:]

        for i in range(len(start)):
            result.append(start[i])
            result.append(end[i])

    else: # 카드 수가 홀수일 경우
        start = card[:(len(card)//2 +1)]
        end = card[len(card)//2 +1:]

        for i in range(len(end)):
            result.append(start[i])
            result.append(end[i])

    if len(card)%2 == 0:
        print('#{}'.format(tc), *result)
    else:
        result.append(start[-1])
        print('#{}'.format(tc), *result)