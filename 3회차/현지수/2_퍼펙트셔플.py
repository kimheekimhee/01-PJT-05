import sys

sys.stdin = open("_퍼펙트셔플.txt")

t = int(input())
for test_case in range(1, t + 1):
    n = int(input())
    cards = list(input().split())
    # 첫번째 카드뭉치
    fir = []
    # 두번째 카드뭉치
    sec = []
    # 카드수가 홀수인지 짝수인지에 따라 카드뭉치 구분
    # 짝수라면
    if len(cards) % 2 == 0:
        for i in range(len(cards)):
            if i < len(cards) // 2:
                # 중앙값 포함x(없음)
                fir.append(cards[i])
            else:
                sec.append(cards[i])
    # 홀수라면
    if len(cards) % 2 == 1:
        for i in range(len(cards)):
            # 중앙값 포함
            if i <= len(cards) // 2:
                fir.append(cards[i])
            else:
                sec.append(cards[i])
    
    # 결과 리스트
    result = []
    # 일단 홀짝 구분 없이 마지막 카드 빼고 공통적으로 번갈아가면서 하나씩 넣어줌
    for k in range(len(fir) - 1):
        result.append(fir[k])
        result.append(sec[k])
    # 첫번째 카드뭉치 마지막 카드 넣어줌
    result.append(fir[-1])
    # 홀수면 끝이겠지만 짝수면 두번째 카드뭉치에 마지막 카드 한장 남아있음
    if len(fir) == len(sec):
        # 마지막 카드 추가
        result.append(sec[-1])
    print(f'#{test_case}', *result)
