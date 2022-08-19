import sys

sys.stdin = open("_모음이보이지않는사람.txt")


t = int(input())

for tc in range(1, t+1):
   
    string = input()
    vowel_blind = ''

    for vowel in range(len(string)):
        if string[vowel] in ['a', 'e', 'i', 'o', 'u']:
            continue
        vowel_blind += string[vowel]

    print(f'#{tc} {vowel_blind}')


