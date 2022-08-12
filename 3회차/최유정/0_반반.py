import sys

sys.stdin = open("_반반.txt")


TC = int(input())

for i in range(1, TC+1):
    S = input()
    s_dic = {}
    for s in S:
        if s in s_dic:
            s_dic[s] += 1
        else:
            s_dic[s] = 1
    if len(s_dic) == 2 and sum(s_dic.values()) == 4:
        print(f'#{i} Yes')
        
    else:
        print(f'#{i} No')
        
