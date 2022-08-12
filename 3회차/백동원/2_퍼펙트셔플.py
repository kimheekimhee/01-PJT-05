import sys

sys.stdin = open("_퍼펙트셔플.txt")
T = int(input())
for _ in range(1, T + 1):
    word = int(input())
    word_list = input().split()
    front = []
    back = []
    result = []
    number = 0
    for a in range(word):
        if word % 2 == 0:
            if a < word/2:
                front.append(word_list[a])
            else:
                back.append(word_list[a])
        else:
            if a < ((word // 2) + 1):
                front.append(word_list[a])
            else:
                back.append(word_list[a])
    while len(result) != word:
        result.append(front[number])
        if len(result) == word:
            break
        result.append(back[number])
        number += 1
    print(f'#{_}', end= ' ')
    for b in result:
        print(b, end = ' ')
    print()