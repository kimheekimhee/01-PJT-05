import sys

sys.stdin = open("_반반.txt")

t = int(input())

for i in range(1, t + 1):
    s = input()
    chk = set(s)
    cnt = 0
    result = False

    if len(chk) == 2:
        for j in chk:
            if s.count(j) == 2:
                cnt += 1

        if cnt == 2:
            result = True

    if result:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')
