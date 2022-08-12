import sys

sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())

for tc in range(1, t+1):

    n = int(input())
    card = list(input().split())
    divided_1 = []
    divided_2 = []
    shuffled_deck = [] 

    if n % 2 == 0:  # If it's an even numbers of cards, divide in half and append the cards in list divided_1 and 2 evenly
                    # 
        