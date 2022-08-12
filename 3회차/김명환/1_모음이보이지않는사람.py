import sys

sys.stdin = open("_모음이보이지않는사람.txt")
vowels = ['a', 'e', 'i', 'o', 'u']
T = int(input())
for i in range(T):
    word = input()
    result = ''
    for j in word:
        if j not in vowels:
            result += j
    print(f'#{i+1} {result}')