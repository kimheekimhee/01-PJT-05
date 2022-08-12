import sys

sys.stdin = open("_반반.txt")
T = int(input())
for _ in range(1, T + 1):
    check = True
    word = input()
    kind = set(list(word))
    if len(kind) == 2:
        for a in range(2):
            if word.count(list(kind)[a]) != 2:
                check = False
    else:
        check = False
    if check == True:
        print(f'#{_} Yes')
    else:
        print(f'#{_} No')