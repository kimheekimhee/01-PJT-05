import sys

sys.stdin = open("_퍼펙트셔플.txt")

# 카드를 퍼펙트 셔플 한다는 것은 카드 덱을 정확히 절반으로 나누고
# 나눈 것들에서 교대로 카드를 뽑아 새로운 덱을 만드는 것을 의미
# N개의 카드가 있는 덱이 주어질 때
# 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력
# 만약 N이 홀수이면 교대로 놓을 때
# 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다

# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N이 주어진다
# 두 번째 줄에는 덱에 카드가 놓인 순서대로
# N개의 카드 이름이 공백으로 구분되어 주어진다
# 카드의 이름은 알파벳 대문자와 '-'만으로 이루어짐

# 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를
# 한 줄에 카드 이름을 공백으로 구분하여 출력

# 출력 예시
#1 A D B E C F
#2 JACK KING QUEEN ACE
#3 ALAKIR LORD-JARAXXUS ALEXSTRASZA AVIANA DR-BOOM

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    cardList = []
    l = 0
    r = (N+1) // 2

    for _ in range(N//2):
        cardList.append(cards[l])
        cardList.append(cards[r])
        l, r = l + 1, r + 1

    if N % 2:
        cardList.append(cards[N//2])

    print('#{} {}'.format(tc, ' '.join(map(str, cardList))))