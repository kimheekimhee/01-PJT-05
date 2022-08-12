# 길이 4의 알파벳 대문자 문자열 S
# S에 정확히 두개의 서로 다른 문자 등장
# 각 문자가 정확히 두번 등장하는지 판별
# input line
# test_case_num
# string S
# 조건 O = 'Yes,No
import sys
sys.stdin = open("_반반.txt")

T = int(input())
for test_case in range(1,T+1):
    S = input()
    dic_s = {}
    result = 'Yes'
    for s in S:
        if s not in dic_s:
            dic_s[s] = 1
        else : dic_s[s] += 1
    # print(dic_s)
    if len(dic_s.keys()) != 2 and not dic_s.values() == 2 :
        result = 'No'
    print(f'#{test_case} {result}')