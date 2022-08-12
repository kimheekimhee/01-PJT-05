import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    card = list(input().split())

    if len(card) % 2 ==0:
        first_list = card[:len(card)//2]
        second_list = card[len(card)//2:]
    else:
        first_list = card[:len(card)//2 + 1]
        second_list = card[len(card)//2 + 1:]
    result = []

    while first_list or second_list:
        if first_list:
            result.append(first_list.pop(0))
        if second_list:
            result.append(second_list.pop(0))

    print(f'#{tc}',*result)





