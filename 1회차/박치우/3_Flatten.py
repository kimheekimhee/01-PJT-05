import sys

sys.stdin = open("_Flatten.txt")
test_case = 10
for i in range(test_case):
    dump_count = int(input())
    lst = list(map(int,input().split()))
    score = max(lst) - min(lst)
    for j in range(dump_count):
        lst.sort()
        lst[-1] -= 1
        lst[0] += 1
    print(max(lst) - min (lst))    