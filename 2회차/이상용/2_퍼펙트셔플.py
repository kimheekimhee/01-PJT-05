# 테스트 케이스의 개수
T = int(input())
for _ in range(1, T+1):
  # N장의 카드
  N = int(input())
  card = input().split()

  result = ['']*len(card) # 미리 만들어놔야 순서가 안 꼬임!
  # 카드가 홀수일 때
  if N % 2:
    for i in range(N // 2 + 1):
      result[2 * i] = card[i]
    for i in range(N // 2):
      result[2 * i + 1] = card[i  + N // 2 + 1]
  # 카드가 짝수일때
  else:
    for i in range(N // 2):
      result[2 * i] = card[i]
      result[2 * i + 1] = card[i + N // 2]

  print(f'#{_}',*result)