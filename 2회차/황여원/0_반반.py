import sys

sys.stdin = open("_반반.txt")

T = int(input())
for tc in range(1,T+1) : 
    # 길이 4의 알파벳 대문자로 이루어진 문자열 S
    S = list(input())
    # print(set(S))
    # set을 사용하여 중복을 제거했을 때 똑같은 문자열이 두개씩 있는 경우, 리스트에 2개만 남아야 함 

    # 중복 제거 
    word = set(S)

    # 중복을 제거한 문자의 길이가 2가 아니면 no, 2이면 yes 
    if len(word) != 2 : 
        print(f'#{tc} No')
    elif len(word) == 2 : 
        print(f'#{tc} Yes')