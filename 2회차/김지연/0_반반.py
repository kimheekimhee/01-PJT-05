import sys

sys.stdin = open("_반반.txt")


n = int(input())
for _ in range(n):
    s = input()
    
    cnt = 1
    s_list = []
    result = []
    for char in s:
        if char not in s_list:
            s_list.append(char)
        else:
            cnt += 1
            result.append(cnt)
            cnt = 1

    if len(result) == 2 and result[0] == 2 and result[1] == 2:
        print('#{} Yes'.format(_+1))
        
    else:
        print('#{} No'.format(_+1))
        