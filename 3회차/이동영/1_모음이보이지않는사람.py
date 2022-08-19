import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

for tc in range(T):
    str_ = ''
    str_ = input()

    for i in str_:
        if i in 'aeiou':
            str_ = str_.replace(i,'')

    print(f'#{tc+1}', str_)