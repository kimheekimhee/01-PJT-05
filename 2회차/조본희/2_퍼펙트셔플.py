import sys
sys.stdin = open("_퍼펙트셔플.txt")

T = int(input())

for test_case in range(1, T + 1):
    n = int(input())
    cards = list(input().split())
    idx = n // 2 if n % 2 == 0 else n // 2 + 1 #홀수일경우 1번덱에 1개 더주기
    cards1 = cards[0 : idx]
    cards2 = cards[idx : ]
    ans = []

    for i in range(idx):
        try:
            ans.append(cards1[i])
            ans.append(cards2[i]) # 홀수일 경우 index에러나니 try except로 구현
        except:
            pass
    
    print(f'#{test_case} {" ".join(map(str, ans))}')