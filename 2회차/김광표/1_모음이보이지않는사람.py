import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
vowel = ['a', 'e', 'i', 'o', 'u']
for i in range(1, T+1) :
    word = input()
    nword = ''
    for char in word :
        if char not in vowel :
            nword += char
    print('#%d'%i, nword)