import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for t in range(T):
    card_cnt = int(input())
    card = list(input().split())
    
    card2 = []
    ans = []
    if card_cnt % 2 == 0:
        for i in range(card_cnt // 2):
            card2.append(card.pop()) # 거꾸로 푸시됨
        for j in range(card_cnt // 2):
            ans.append(card[j])
            ans.append(card2[::-1][j])
    else:
        for x in range(card_cnt // 2):
            card2.append(card.pop())
        for y in range((card_cnt // 2)+1):
            ans.append(card[y])
            if y != len(card2):
                ans.append(card2[::-1][y])
            else:
                pass
    
    print(f'#{t+1}',*ans)