import sys
sys.stdin = open("_모음이보이지않는사람.txt")
info = ['a','e','i','o','u']
T = int(input())

for test_case in range(1,T+1):
    s = input()
    count=0
    stack = []
    for i in s:
        for j in range(len(info)):
            if i == info[j]:
                count += 1
        if count == 0:
            stack.append(i)
        else:
            count = 0
    print(f'#{test_case}',end=' ')
    print(''.join(stack))
