# import sys

# sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())
for i in range(1,t+1):
    n = int(input())
    cards = list(input().split())
    newcards = []
    if n%2 == 0:
        first_cards = cards[:int(n/2)]
        second_cards = cards[int(n/2):]
        for _ in range(int(n/2)):
            newcards.append(first_cards[_])
            newcards.append(second_cards[_])
    else :
        first_cards = cards[:(n//2)+1]
        seconds_cards = cards[(n//2)+1:]
        newcards.append(first_cards[0])
        for _ in range(n//2):
            newcards.append(seconds_cards[_])
            newcards.append(first_cards[_+1])
    print(f"#{i}",*newcards)

