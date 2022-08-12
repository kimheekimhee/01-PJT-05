import sys

sys.stdin = open("_퍼펙트셔플.txt")


from collections import deque
T = int(input())

for tc in range(1, T+1):
    card_num = int(input())
    cards_lst = input().split()
    
    med = card_num // 2   
     
    # 반올림이 기억이 안나서
    if card_num % 2 == 0:
        slicer = med
    else:
        slicer = med + 1
    
    lst_1 = deque(cards_lst[:slicer])
    lst_2 = deque(cards_lst[slicer:])
    
    lst_1_size = len(lst_1)
    lst_2_size = len(lst_2)

    print(f'#{tc} ',end='')
    count = 0
    
    while True:
        if count < lst_1_size:
            print(lst_1.popleft(), end=' ')
            
        if count < lst_2_size:
            print(lst_2.popleft(), end=' ')
        count += 1
        
        if count >= lst_1_size and count >= lst_2_size:
            break
    print()