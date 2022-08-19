# N개의 카드가 있는 덱이 주어질 때 이를 퍼펙트 셔플하면 어떤 순서가 되는지 출력하는 프로그램을 작성하라.

# 만약 N이 홀수이면, 교대로 놓을 때 먼저 놓는 쪽에 한 장이 더 들어가게 하면 된다.


# [입력]
# 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에는 자연수 N(1 ≤ N ≤ 1,000)이 주어진다.
# 두 번째 줄에는 덱에 카드가 놓인 순서대로 N개의 카드 이름이 공백으로 구분되어 주어진다.
# 카드의 이름은 알파벳 대문자와 ‘-’만으로 이루어져 있으며, 길이는 80이하이다.

# [출력]

# 각 테스트 케이스마다 주어진 덱을 퍼펙트 셔플한 결과를 한 줄에 카드 이름을 공백으로 구분하여 출력한다.

import sys

sys.stdin = open("_퍼펙트셔플.txt")


T = int(input())
for tc in range(1,T+1):
# N장의 카드
    N = int(input())
    card = input().split()
    result = []*len(card)
    
# 홀수 
    if N%2:
        for i in range(N//2+1):
            result[2*i] = card[i]

        for i in range(N//2):
            result[2*i+1] = card[i+N//2+1]
# 짝수 
    else:
        for i in range(N//2):
            result[2*i] = card[i]
            result[2*i+1] = card[i+N//2]
    print(f'#{tc}',*result)