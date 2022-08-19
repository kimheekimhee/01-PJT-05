import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(sys.stdin.readline())

for i in range(1,T+1):
    N = int(sys.stdin.readline())
    cards = list(map(str,sys.stdin.readline().split()))
    left_card = []
    right_card = []
    new_cards = []
    if N % 2 == 0:
        for j in range(N//2):
            left_card.append(cards[j])
        for k in range(j+1,len(cards)):
            right_card.append(cards[k])
        while right_card:
            new_cards.append(left_card.pop(0))
            new_cards.append(right_card.pop(0))
    else:
        for j in range(N//2+1):
            left_card.append(cards[j])
        for k in range(j+1,len(cards)):
            right_card.append(cards[k])
        while left_card:
            if not right_card:
                new_cards.append(left_card.pop(0))
                break
            new_cards.append(left_card.pop(0))            
            new_cards.append(right_card.pop(0))
    print(f"#{i}",end=" ")
    for _ in new_cards:
        print(_,end=" ")
    print()
