import sys

sys.stdin = open("_반반.txt")

for test_case in range(1, int(input()) + 1):
    # 중복제거해서 문자가 두개라면 길이가 2개 임을 이용
    s = set(input())
    if len(s) == 2:
        print(f"#{test_case} {'Yes'}")
    else:
        print(f"#{test_case} {'No'}")