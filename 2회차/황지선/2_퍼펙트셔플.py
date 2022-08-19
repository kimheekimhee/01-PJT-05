import sys

sys.stdin = open("_퍼펙트셔플.txt")

# 셔플방식
# 123456
# 123 / 456
# 1 4 2 5 3 6

# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.
# 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.


# 출력
# 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.


# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
T = int(input())

for t in range(T):
    # 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.    
    N = int(input())
    # 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
    card = list(input().split())

    if N % 2 == 0: # N이 짝수개일 경우
        num = N // 2
    else:
        num = N // 2 + 1


    f_card = card[:num]
    b_card = card[num:]

    # print(f_card)
    # print(b_card)   
    # ['A', 'B', 'C']
    # ['D', 'E', 'F']
    # ['JACK', 'QUEEN']
    # ['KING', 'ACE']
    # ['ALAKIR', 'ALEXSTRASZA', 'DR-BOOM']
    # ['LORD-JARAXXUS', 'AVIANA']

    for l in range(1, len(card), 2):    
        f_card.insert(l, b_card[0])
        del b_card[0]

    print(f'#{t+1}', *f_card)