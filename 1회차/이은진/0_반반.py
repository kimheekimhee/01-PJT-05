import sys

sys.stdin = open("_반반.txt")

for t in range(1,int(input())+1):
    word = input()
    check = dict()
    for w in word:
        if w not in check.keys():
            check[w] = 1
        else:
            check[w] += 1
    if len(check) == 2 and max(check.values()) == 2:
        print(f'#{t} Yes')
    else:
        print(f'#{t} No')