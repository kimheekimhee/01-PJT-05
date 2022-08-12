import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(T):
    s = input()
    freq = {}

    for char in s:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1

    if len(freq) != 2:
        print(f'{tc} No')
    else:
        f2 = True
        for f in freq.values():
            if f != 2:
                f2 = False
                break
        if f2:
            print(f'{tc} Yes')
        else:
            print(f'{tc} No')
