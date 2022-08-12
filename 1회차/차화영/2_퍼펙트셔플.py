import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    card = list(input().split())
    l1 = []
    l2 = []

    if len(card)%2 == 0:
        half = n//2
        l1 = card[0:half] # append를 사용하면 [[]] 형태가 된다.
        l2 = card[half:]
        
    else:
        half2 = (n+1)//2
        l1 = card[0:half2]
        l2 = card[half2:]
    answer = []
    while len(l1) != 0 or len(l2) != 0:
        if len(l1) != 0:
            answer.append(l1.pop(0))
        if len(l2) != 0:
            answer.append(l2.pop(0))
    print(f'#{tc}', *answer)