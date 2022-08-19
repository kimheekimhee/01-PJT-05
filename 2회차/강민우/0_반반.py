import sys

sys.stdin = open("_반반.txt")
T = int(input())
for tc in range(1, T+1):
    S = input()
    S_dic = {}
    for a in S:
        S_dic[a] = S_dic.get(a, 0) +  1
    cnt = 0
    for a in S_dic:
        if S_dic[a] == 2:
            cnt += 1
    if cnt == 2:
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')