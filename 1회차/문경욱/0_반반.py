# import sys

# sys.stdin = open("_반반.txt")

# 문자열을 입력 받은 뒤 set로 변환한 후 길이가 2인지 검사
# 2인 경우 원래 문자열을 count를 이용해서 2가 아닌 것이 있으면 NO 출력, 전부 2면 Yes 출력
# 위의 방법으로 간단하게 풀 수 있지만 딕셔너리에 익숙해졌고, 앞으로도 계속 유용하게 사용할 것 같아서 딕셔너리를 활용해서 풀었습니다.

T = int(input())

for test_case in range(1, T+1):
    # 조건에 맞는지 확인을 위한 boolen 변수 설정
    is_ok = True
    
    S = input()

    # 문자열을 딕셔너리 형태로 저장
    dict_ = {}

    # 글자가 딕셔너리 안에 없으면 1로 초기화, 안에 있으면 +1
    for alpha in S:
        dict_[alpha] = dict_.get(alpha,0) +1

    # 입력이 두 글자가 아니면 종류가 아니면 False
    if len(dict_) != 2:
        is_ok = False
    # 입력이 두 글자인데
    else:
        # 밸류 값이 2가 아닌게 있으면, 즉 나온 횟수가 2가 아니면 False
        for v in dict_.values():
            if v != 2:
                is_ok = False
            else:
                continue
            
    # is_ok가 참이면
    if is_ok == True:
        print(f'#{test_case} Yes')
    else:
        print(f'#{test_case} No')
    #print(dict_)