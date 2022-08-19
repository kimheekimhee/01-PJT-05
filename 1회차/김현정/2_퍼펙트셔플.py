import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
result = []

for _ in range(1, T+1):
    N = int(input())
    card_list = list(input().split())
    card_list1 = []
    card_list2 = []
    card_result = []
    card_half1 = 0
    card_half2 = 0

    # N이 짝수일 때
    if N % 2 == 0:

        # 카드 반반씩 나누기
        card_half1 = len(card_list) // 2
        
        for i in range(0, card_half1):
            card_list1.append(card_list[i])
        for j in range(card_half1, len(card_list)):
            card_list2.append(card_list[j])

        # 반 나눈 카드를 셔플하여 card_result에 넣기
        for k in range(0, card_half1):
            card_result.append(card_list1[k])
            card_result.append(card_list2[k])
    
    # N이 홀수일 때
    else:

        # 카드 첫번째 더미에 하나 더 넣는 것으로 반 나누기
        card_half1 = (len(card_list) // 2) + 1
        card_half2 = len(card_list) // 2
        
        for i in range(0, card_half1):
            card_list1.append(card_list[i])
        for j in range(card_half1, len(card_list)):
            card_list2.append(card_list[j])

        # 반 나눈 카드를 셔플하여 card_result에 넣기, 단 첫번째 더미 마지막 카드는 안들어감
        for k in range(0, card_half2):
            card_result.append(card_list1[k])
            card_result.append(card_list2[k])
        
        # 첫번째 더미 마지막 카드 넣기
        card_result.append(card_list1[card_half1-1])
    
    # 결과를 리스트에 담기
    print(f"#{_}", card_result)