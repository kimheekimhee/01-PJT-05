import sys

sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())

for tc in range(1,t+1):
    n = int(input())
    card = list(input().upper().split()) #대문자로받아주기
    l_card = len(card)
    
    if l_card % 2 == 0 :#짝수면
        x = card[:l_card// 2] #처음부터 반까지
        y = card[l_card// 2:] # 반부터 끝까지
    else: #홀수면
        x = card[:l_card// 2+1] #처음부터 반까지
        y = card[l_card// 2+1:] # 반부터 끝까지
    # print(x,y)
    # ['A', 'B', 'C'] ['D', 'E', 'F']
    # ['JACK', 'QUEEN'] ['KING', 'ACE']
    # ['ALAKIR', 'ALEXSTRASZA', 'DR-BOOM'] ['LORD-JARAXXUS', 'AVIANA']

    ans = [] #빈리스트에 맨처음요소 하나씩 빼서 넣기
    for i in range(l_card):
        if x:
            ans.append(x.pop(0))
        if y:
            ans.append(y.pop(0))
    print(f'#{tc}', *ans)
