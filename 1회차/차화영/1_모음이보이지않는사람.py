import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
collection = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T+1):
    cantsee = []
    word = input()
    ans = ''
    for i in word:
        if i in collection:
            continue
        else:
            cantsee.append(i)
    print("#{} {}".format(tc, ''.join(cantsee)))