import sys

sys.stdin = open("_반반.txt")

T = int(input()) # 테스트 케이스 개수

for test_case in range(T):
    my_dict = {} # 문자 별로 나눠서 정리할 딕셔너리
    S = input()

    for i in S: # 문자 하나하나를 밸류와 함께 저장
        if i not in my_dict:
            my_dict[i] = 1
        else:
            my_dict[i] += 1

    cnt = 0 # value가 2인 갯수를 계산하기위한 변수
    if len(my_dict) == 2: # 먼저 딕셔너리에 키값이 두 개 인지 판별
        for v in my_dict.values(): # 순회하면서 밸류 가 2인 문자 카운트
            if v == 2:
                cnt += 1
        if cnt == 2: # 밸류가 2인것들 도 두 개일때.
            print(f'#{test_case+1} Yes')
        else:
            print(f'#{test_case+1} No') # 아닐때.
    else:
        print(f'#{test_case+1} No') # 키값이 두 개가 안될때