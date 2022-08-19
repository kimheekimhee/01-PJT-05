# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, S에 정확히 두 개의 서로 다른 문자가 등장하고, 각 문자가 정확히 두 번 등장하는 지 판별하라.

import sys

sys.stdin = open("_반반.txt")

TC = int(input())
for t in range(1,TC+1):
    S = input()
    # 조건 : 두개의 문자가 각각 두번씩 등장한다.

    # 등장하는 문자 저장
    c_dict = {}
    set_S = set(S)
    for i in set_S:
        c_dict[i]=0 # 문자의 개수 == 0 설정

    # 문자의 개수 저장
    for i in c_dict:
        for j in range(len(S)):
            if i==S[j]:
                c_dict[i]+=1

    # 조건 충족 여부
    # 1.문자의 개수 : 2개. 2.두번씩 등장
    if len(c_dict)==2: # 1
        for i in c_dict:
            if c_dict[i]==2: # 2
                answer = "Yes"
    else:
        answer = "No"
    print(f"#{t} {answer}")
