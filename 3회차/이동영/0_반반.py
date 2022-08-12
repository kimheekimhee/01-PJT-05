import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(T):
    
    dict_ = dict()
    str_ = input()

    for i in str_:
        if i in dict_:
            dict_[i] += 1

        else: 
            dict_[i] = 1
    cnt = 0
    for i in list(dict_.values()):
        if i == 2:
            cnt += 1

    if cnt == 2:
        print(f'#{tc+1}' ,'Yes')
    else:
        print(f'#{tc+1}' ,'No')   