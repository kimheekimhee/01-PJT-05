import sys

sys.stdin = open("_퍼펙트셔플.txt")

# 반씩 우선 나눠주는 프로그램

T = int(input())

for n in range(1, T+1):
    num = int(input())
    cards_n = input().split()
    if num % 2 == 0:
        half = num // 2
        list_1 = cards_n[:half]
        list_2 = cards_n[half:]
    else:
        list_1 = cards_n[:half+1]
        list_2 = cards_n[half+1:]

    result_deck = [0] * num
    for i in range(num):
        if i % 2 == 0:
            result_deck[i] = list_1.pop(0)
        else:
            result_deck[i] = list_2.pop(0)

    print(f'#{n}', *result_deck)
    
    

        

    
        


        