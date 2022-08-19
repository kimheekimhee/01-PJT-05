import sys

sys.stdin = open("_모음이보이지않는사람.txt")

# 문제풀이

T = int(input())

for tc in range(1, T + 1):
    word = input()

    a = word.replace('a', '')  # 문자열에서 모음을 하나씩 삭제 (변환)
    e = a.replace('e', '')
    i = e.replace('i', '')
    o = i.replace('o', '')
    u = o.replace('u', '')

    print(f'#{tc} {u}')
