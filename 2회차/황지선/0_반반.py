import sys

sys.stdin = open("_반반.txt")


# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때, 
 

# 출력
# 각 테스트 케이스마다
#     ∙ 조건이 만족되면 “Yes”, 


# 첫 번째 줄에 테스트 케이스의 수 TC가 주어진다.
TC = int(input())

# 이후 TC개의 테스트 케이스가 새 줄로 구분되어 주어진다.
for t in range(TC):
    # 첫 번째 줄에 문자열 S가 주어진다.
    S = input()
    dict_ = {}
    res = 'No' # 기본값

    # 문자열에 담긴 알파벳 숫자 세어서 dict_에 정리하기
    for s in range(len(S)):
        if S[s] not in dict_:
            dict_[S[s]] = 1
        else:
            dict_[S[s]] += 1
    
    # print(dict_)
    # {'A': 2, 'B': 2}
    # {'C': 2, 'D': 2}
    # {'E': 2, 'F': 2}
    # {'E': 4}
    # {'N': 2, 'O': 1, 'E': 1}

    # print(dict_.values())

    # S에 정확히 두 개의 서로 다른 문자가 등장하고,
    # 각 문자가 정확히 두 번 등장하는 지 판별하라.
    if len(dict_) == 2:
        for d in dict_.values():
            if d == 2:
                res = 'Yes'
            else:
                res = 'No'

    # # 아니면 “No” 를 출력하라.
    # else:
    #     res = 'No'

    print(f'#{t+1} {res}')