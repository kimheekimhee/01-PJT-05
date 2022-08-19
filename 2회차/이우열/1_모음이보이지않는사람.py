import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
mo = ['a', 'e', 'i', 'o', 'u']

for i in range(1, t + 1):
    s = input()

    for j in s:
        if j in mo:
            s = s.replace(j, '')

    print(f'#{i} {s}')
