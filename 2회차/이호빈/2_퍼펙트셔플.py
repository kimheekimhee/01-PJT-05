import sys
sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for tc in range(1, T+1):
    #단어 수 
    n = int(input())
    #카드를 리스트에 받아준다
    cards = list(map(str, input().split()))
    #문제에서 원하는 조건데로 주어진 값을 두 가지로 나누는 기준점을 변수에 저장한다.
    mid = n // 2 + n % 2
    #결과값을 담을 리스트
    result = []
    #0부터 n//2 -1 까지 mid를 기준으로 왼쪽에 있는 덱에서 한 개, 오른쪽에 있는 덱에서 한개를 꺼내서 결과값에 넣어준다.
    for k in range(n // 2):
        result.append(cards[k])
        result.append(cards[k + mid])
    #만약 홀수라면
    if n % 2 == 1:
        #가운데 값에 마지막 요소를 넣어준다.
        result.append(cards[n // 2])

    print(f"#{tc}", end = " ")
    print(*result)

