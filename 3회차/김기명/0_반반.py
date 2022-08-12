import sys

sys.stdin = open("_반반.txt")

# 길이4 대문자 단어S가 주어짐. S에 정확히 두개의 서로다른 문자가 등장하고, 둘다 두번등장하는지 판별하기.

T = int(input())
for test_case in range(1, T + 1):
    S = input()
    dic_s = {}
    for i in S:
        if i not in dic_s:
            dic_s[i] = 1
        else:
            dic_s[i] += 1

    if len(dic_s) != 2:                     # 문자열 S의 알파벳이 두개가 아니면 틀린것.
        print(f'#{test_case} No')
        continue

    cnt = 0        #여기까지왔으면 알파벳이 두개기떄문에 변수2개 설정 (몇번나왔는지 확인)
    
    for i in dic_s:
        if dic_s[i] == 2:
            cnt += 1
    
    if cnt == 2:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')