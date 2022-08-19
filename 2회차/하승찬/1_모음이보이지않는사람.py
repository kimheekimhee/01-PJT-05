import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):


    mo= 'a', 'e', 'i', 'o', 'u'


    n= input()

    word =[]
    for char in n:
        if char in mo:
            continue
        word.append(char)
    print(f'#{test_case}',end=' ')
    print(*word,sep='')