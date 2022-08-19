import sys

sys.stdin = open("_퍼펙트셔플.txt")
t = int(input())
for _ in range(1,t+1):
    card_r = []
    card_l = []
    n = int(input())
    a = list(map(str, input().split()))
    # print(a)
    if len(a) % 2 == 0:
       
        card_r = (a[0:n//2])
        card_l = (a[n//2:])
    else :
        card_r = (a[0:n//2+1])
        card_l = (a[n//2+1:])

    res = []
    for p in range(n):
        if p % 2 == 0:
            res.append(card_r.pop(0))
        elif p % 2 == 1: 
            res.append(card_l.pop(0))
    
    print(f'#{_}', *res)



