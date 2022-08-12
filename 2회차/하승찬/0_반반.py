import sys

sys.stdin = open("_반반.txt")


T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):

    word = input()


    alp = [0]*26



    for c in word:
        alp[ord(c)-65]+=1

    cnt= 0
    for ac in alp:
        if ac ==2:
            cnt+=1


    if cnt==2:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
