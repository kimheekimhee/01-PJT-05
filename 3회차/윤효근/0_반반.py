import sys

sys.stdin = open("_반반.txt")
T = int(input())
for test_case in range(T):
    count = 0
    s = input()
    result=[]
    for i in s:
        result.append(s.count(i))
    for i in result:
        if i == 2:
            count += 1
    if count == 4:
        print(f'#{test_case +1} Yes')
    else:
        print(f'#{test_case+ 1} No')
