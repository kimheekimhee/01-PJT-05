import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(T):

    card = int(input())
    card_list = []
    card_list = list(input().split())
    new_list = []
    
    if card % 2 == 0:
        card1 = card_list[0:(len(card_list)//2)]
        card2 = card_list[(len(card_list)//2):]
        for i in range(0,len(card2)):
            new_list.append(card1[i])
            new_list.append(card2[i])
        print(f'#{tc+1}',' '.join(new_list))
    
    if card % 2 == 1:
        card1 = card_list[0:(len(card_list)//2)+1]
        card2 = card_list[(len(card_list)//2)+1:]
        
        
        for i in range(0,len(card1)):
                if i == len(card2) : 
                    new_list.append(card1[i])
                    break
                else:
                    new_list.append(card1[i])
                    new_list.append(card2[i])
        print(f'#{tc+1}',' '.join(new_list))      