import sys

sys.stdin = open("_모음이보이지않는사람.txt")
test_case = int(input())
vowel = ['a','e','i','o','u']
for i in range(test_case):
    word = input()
    lst = []
    for i in word:
        if i not in vowel:
            lst.append(i)
    lst = ''.join(lst)
    print(lst)

