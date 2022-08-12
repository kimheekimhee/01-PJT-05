import sys

sys.stdin = open("_퍼펙트셔플.txt")


T = int(input())
for i in range(1, T+1):
    N = int(input())
    cards = input().split()
    
    a_deck = []
    b_deck = []
    new_deck = []

    for j in range(len(cards)):
        if j < len(cards)/2:
            a_deck.append(cards[j])
        else:
            b_deck.append(cards[j])

    for j in range(N):
        if j % 2 ==0:
            a = a_deck.pop(0)
            new_deck.append(a)
        else:
            b = b_deck.pop(0)
            new_deck.append(b)

    print(f"#{i} {' '.join(new_deck)}")