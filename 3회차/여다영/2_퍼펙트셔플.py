import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for _ in range(1, T + 1):
    num = int(input())

    if num % 2 == 0:
        split_num = num // 2

        deck = input().split()
        deck_1 = []
        for i in range(split_num):
            deck_1.append(deck[i])
        deck_2 = []
        for i in range(split_num, len(deck)):
            deck_2.append(deck[i])

        perfect_shuffle = []
        for i in range(split_num):
            perfect_shuffle.append(deck_1[i])
            perfect_shuffle.append(deck_2[i])
    else:
        split_num = num // 2 + 1
        
        deck = input().split()
        deck_1 = []
        for i in range(split_num):
            deck_1.append(deck[i])
        deck_2 = []
        for i in range(split_num, len(deck)):
            deck_2.append(deck[i])

        perfect_shuffle = []
        for i in range(split_num - 1):
            perfect_shuffle.append(deck_1[i])
            perfect_shuffle.append(deck_2[i])
        perfect_shuffle.append(deck_1[split_num - 1])

    print(f'#{_}', *perfect_shuffle)
