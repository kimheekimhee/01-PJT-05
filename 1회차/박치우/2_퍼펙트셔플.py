import sys

sys.stdin = open("_퍼펙트셔플.txt")
test_case = int(input())
for i in range(test_case):
    count = int(input())
    holsu = count
    word = input().split()
    if count % 2 == 0:
        count = count // 2
    else:
        count = count // 2
    lst = []
    for j in range(count):
        lst.append(word.pop())
    lst.reverse()
    print('#{0}'.format(i+1),end = ' ')
    for k in range(len(lst)):
        print(word[k],end = ' ')
        print(lst[k],end = ' ')
    if holsu % 2 == 1:
        print(word[-1])
    print()
