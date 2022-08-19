import sys

sys.stdin = open("_퍼펙트셔플.txt")
t = int(input())
for test in range(1,t+1):
    n = int(input())
    card_list = []

    card = list(map(str,input().split()))
    if n / 2 == 0:
        for i in range(n//2):
            card_list.append(card[n-n+i])
            card_list.append(card[n//2+i])
    else:
        for j in range(n//2):
            card_list.append(card[n-n+j])
            card_list.append(card[n//2+j])


        
    print(f'#{test}',*card_list)
    #print(f'#{test} {card[n-n]} {card[n//2]} {card[n-n+1]} {card[n//2+1]}')
