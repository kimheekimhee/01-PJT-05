import sys
sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for i in range(T):
    N = int(input())
    mid_num = N // 2
    card_li = list(input().split())
    temp = []
    if N % 2 == 0:
        for j in range(mid_num):
            temp.append(card_li[j])
            temp.append(card_li[j+mid_num])     
    else: 
        for j in range(mid_num):
            temp.append(card_li[j])
            temp.append(card_li[j+mid_num+1])   
        temp.append(card_li[mid_num])   
    print(f'#{i+1}',end=' ')
    print(*temp)