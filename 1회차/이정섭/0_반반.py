import sys

sys.stdin = open("_반반.txt")

t = int(input())

for tc in range(1, t+1):
    s = list(input())
    end = True

    for i in s:
        if s.count(i) == 2:
           pass

        else:
            end = False
            break

    if end == True:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')



