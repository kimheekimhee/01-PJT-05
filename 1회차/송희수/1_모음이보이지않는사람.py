import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
unlook_word = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, T+1):
    word =input()
    word_list =[]
    for n in word:
        word_list.append(n)
    for x in range(len(word_list)):
        for y in unlook_word:
            if y in word_list:
                word_list.remove(y)
    print('#%d' % tc,end=" ")
    for k in word_list:
        print(k, end ="")
    print()