import sys

sys.stdin = open("_퍼펙트셔플.txt")
T = int(input())
for i in range(1, T+1):
    N = int(input())
    card = input().split()
    if N % 2 == 1:
        n2 = N//2 + 1
    else:
        n2 = N//2
    card1 = card[0:n2]; card2 = card[n2:N]
    new_card = []
    for j in range(len(card1)):
        new_card.append(card1[j])
        if j < len(card2):
            new_card.append(card2[j])
    print(f'#{i}', *new_card)