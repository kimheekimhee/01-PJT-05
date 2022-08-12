import sys

sys.stdin = open("_퍼펙트셔플.txt")
t = int(input())
for i in range(1, t + 1):
    n = int(input())
    lst = list(map(str, input().split()))
    lst1 = lst[:(n + 1) // 2]
    lst2 = lst[(n + 1) // 2:]
    print('#{}'.format(i), end = ' ')
    for j in range(len(lst2)):
        print(lst1[j], lst2[j], end = ' ')
    if n % 2 == 1:
        print(lst1[-1], end = ' ')
    print()
    