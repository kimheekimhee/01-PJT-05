import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
for t in range(1, T+1):
    print(f'#{t}', end=' ')
    word = input()
    for i in word:
        # 문자가 모음이라면
        if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
            # 건너뛰기
            continue
        # 문자가 자음이라면
        else:
            # 자음 출력
            print(i, end='')
    print()