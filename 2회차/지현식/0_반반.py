import sys

sys.stdin = open("_반반.txt")

for test_case in range(1, int(input()) + 1):
    # 입력
    s = input()
    # 딕셔너리
    dic = {}
    # 중복 출력 방지을 위한 flag
    check = False

    for i in s:
        dic[i] = dic.get(i, 0) + 1
    # 딕셔너리의 value 값이 2가 아니면 해당 input 은 문자이다.
    for v in dic.values():
        if v != 2:
            check = True
            print(f"#{test_case} {'No'}")
            break
    if not check:
        print(f"#{test_case} {'Yes'}")