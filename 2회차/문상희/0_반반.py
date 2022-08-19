import sys

sys.stdin = open("_반반.txt")

test_case = int(input())
for test in range(1, test_case + 1):
    word = input()
    check = 1
    for i in word:
        if word.count(i) != 2:
            check = 0
    if check == 1:
        print(f'#{test} Yes')
    else:
        print(f'#{test} No')
# 문자열이 4개의 문자로 이루어졌고 2개의 문자가 2개씩 있는지 확인하므로 문자열을 순회하며 2개가 아닌 문자가 나오면 조건에 맞지 않습니다.