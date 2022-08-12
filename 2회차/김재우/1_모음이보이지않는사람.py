import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for tc in range(1, T+1):
    word = input()

    new_word = []

    for i in word:
        if i not in 'aeiou':    # 모음 검사
            new_word.append(i)  # 없으면 새로운 단어로 추가

    result = ''.join(new_word)
    
    print(f'#{tc} {result}')

