import sys

sys.stdin = open("_퍼펙트셔플.txt")

T =  int(input())

for tc in range(1,T+1):
    N = int(input())
    cards = list(input().split())
    if N % 2 == 0 :
        f_list = cards[:N//2]
        b_list = cards[N//2:]
    else :
        f_list = cards[:N // 2 + 1]
        b_list = cards[N // 2 + 1:]
    mix_list = []

    while f_list or b_list :
        if f_list :
            mix_list.append(f_list.pop(0))
        if b_list :
            mix_list.append(b_list.pop(0))
    
    print(f'#{tc}', *mix_list)