import sys
from pprint import pprint
sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())

n, m = list(map(int, input().split()))

def shuffle(n, m, cards):
    shuffle_total = 0 # 현재의 셔플 결과

    # 3개의 카드 순회
    for i in range(n -2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                total = cards[i] + cards[j] + cards[k]

                if shuffle_total < total < m: 
                    shuffle_total == total

                if total == m:
                    return total

    return shuffle_total # 셔플한 결과 출력

