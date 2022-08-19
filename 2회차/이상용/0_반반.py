T = int(input())
for _ in range(1, T+1):
  word = input()
  if word[0] == word[1] == word[2] == word[3]:
    print(f'#{_}', 'No')
  elif word[0] == word[1] and word[2] == word[3]:
    print(f'#{_}', 'Yes')
  elif word[0] == word[2] and word[1] == word[3]:
    print(f'#{_}', 'Yes')
  elif word[0] == word[3] and word[1] == word[2]:
    print(f'#{_}', 'Yes')
  else:
    print(f'#{_}', 'No')

    
