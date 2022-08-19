import sys

sys.stdin = open("_퍼펙트셔플.txt")

# list_ = ['A', 'B', 'C', 'D', 'E' , 'F', 'p']
# print(len(list_) //2 +1 )

# 우선 카드 덱을 정확히 절반으로 나누어야 함 
# 카드 갯수가 짝수이면 입력받은 카드 리스트 길이에서 2로 나누면 되고 홀수이면 +1 을 해주어야 함 
T = int(input())
for tc in range(1, T + 1) : 
    N = int(input()) 
    card = list(input().split())

    # 카드 갯수가 짝수이면 
    if len(card) % 2 == 0 : 
        # 반으로 나누기 
        a_card = card[:len(card) // 2]
        b_card = card[len(card)// 2 :]

    # 카드 갯수가 홀수면 
    else : 
        a_card = card[:len(card) // 2 +1]
        b_card = card[len(card)// 2 +1 :]

    # print(a_card, b_card)
    
    # 반으로 나눈걸 번갈아가면서 담아줘야한다.. 
    # 빈 리스트를 만들어주고 
    result = []
   
    while a_card or b_card : 
        # 만약 a_card에 존재하면 result에 a_card의 젤 첫번째꺼를 pop해서 담아주고 
        # b_card면 똑같이 젤 첫번째꺼 pop해서 담아주기 
        if a_card :
            result.append(a_card.pop(0))
        if b_card :
            result.append(b_card.pop(0))
    
    print(f'#{tc}', *result) 