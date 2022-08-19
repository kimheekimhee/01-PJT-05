# 테스트케이스 입력
T = int(input())
# 케이스별로 단어 입력
for _ in range(1, T+1):
  word = input()
  for i in word:
    # 문자열 슬라이싱 + 모음 삭제~~
    if i in 'aeiou':
      word = word.replace(i, "")
  # 테스트 케이스별 출력
  print(f'#{_}', word)