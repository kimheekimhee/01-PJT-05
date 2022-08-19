import sys

sys.stdin = open("_반반.txt")

t =int(input())
for t_case in range(1, t + 1):
    s = input()
    s_dict = {}

    for i in range(len(s)):
            if s[i] not in s_dict.keys():
                s_dict[s[i]] = 1
            else:
                s_dict[s[i]] += 1
    # print(s_dict)
    cnt = list(s_dict.values())
    if len(s_dict.keys()) == cnt.count(2):
        print(f'#{t_case} Yes')
    else:
        print(f'#{t_case} No')
    
