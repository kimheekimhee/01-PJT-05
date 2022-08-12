import sys

sys.stdin = open("_모음이보이지않는사람.txt")

# 모음
alpha = ["a", "e", "i", "o", "u"]
for test_case in range(1, int(input()) + 1):
    result = ""
    s = input()
    for i in s:
        # 모음이 있으면 continue 취급을 하지 않을 것.
        if i in alpha:
            continue
        # 모음이 아니라면 추가
        result += i
    print(f"#{test_case} {result}")