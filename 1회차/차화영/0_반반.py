import sys

sys.stdin = open("_반반.txt")

N = int(input())
for tc in range(1, N+1):
    s = list(input())
    set_ = set(s)
    if len(set_) == 2:
        print("#{} {}".format(tc, 'Yes'))
    else:
        print("#{} {}".format(tc, 'No'))