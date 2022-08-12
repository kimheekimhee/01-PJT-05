import sys

sys.stdin = open("_반반.txt")

T = int(input())

for t in range(1, T+1) :
    cs = input()

    if len(set(cs)) ==  2 and cs.count(cs[0]) == 2 :
        print(f'#{t} Yes')
    else :
        print(f'#{t} No')