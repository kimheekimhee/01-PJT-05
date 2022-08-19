import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(1, T + 1):
    word = input()
    result = 'No'
    set_ = set(word)

    if len(set_) == 2:
        a, b = set_
        if (word.count(a) == 2) and (word.count(b) == 2):
            result = 'Yes'
            
    print(f'#{tc}', result)
