import sys

sys.stdin = open("_반반.txt")

T = int(input())
for t in range(1,T+1):
    s = input()
    # 문자들을 담고 카운트할 딕셔너리
    dic = {}

    # 문자를 딕셔너리에 넣기 위한 반복문
    for i in s:
        # 만약 딕셔너리에 들어있지 않다면
        if i not in dic:
            # 넣고 카운트 1
            dic[i] = 1
        else:
            # 이미 있다면 카운트 1 추가
            dic[i] += 1

    # 딕셔너리 밸류값 꺼내서
    for v in dic.values():
        # 만약 문자가 딱 2개고 카운트도 2개면
        if len(dic) == 2 and v == 2:
            # Yes 출력 후 멈추기
            print(f'#{t} Yes')
            break
        else:
            # 아니라면 No 출력 후 멈추기
            print(f'#{t} No')
            break