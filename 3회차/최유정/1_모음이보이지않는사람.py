import sys

sys.stdin = open("_모음이보이지않는사람.txt")

vowels = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for t in range(1, T+1):
    S = input()
    for s in S:
        if s in vowels:
           S = S.replace(s, "")
    print(f'#{t} {S}')




