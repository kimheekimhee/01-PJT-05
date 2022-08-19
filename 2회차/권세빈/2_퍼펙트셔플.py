import sys

sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())
for t in range(1,T+1):
    n = int(input()) # 카드 개수
    card = input().split() # 카드들
    shuf = [] # 셔플 했을 때의 카드들

    # 슬라이싱으로 뒤에 절반을 new에 넣기
    if n % 2 == 0:
        new = card[n//2:]
    else: # 홀수라면 +1해서 넣기
        new = card[n//2+1:]
    
    # 절반 나눈 카드 수만큼 반복해서
    # 셔플리스트에 번갈아 넣기
    for k in range(len(new)):
        shuf.append(card[k])
        shuf.append(new[k])
    
    # 만약 원래 카드 수와 섞었을 때의 카드 수가 다르다면
    # (카드 수가 홀수라서 한장 남았다면)
    if n != len(shuf):
        # 역순으로 찾아보기
        for h in range(n-1,-1,-1):
            # 절반 나눈 카드도 아니고 셔플한거에도 포함되지 않는 카드를 추가
            if card[h] not in new and card[h] not in shuf:
                shuf.append(card[h])

    print(f'#{t}', *shuf)