import sys

sys.stdin = open("_반반.txt")

a = int(input())

for num in range(1, a+1):
    dic = {}
    word = input()
    for i in word:
        if i in dic:    
            dic[i] += 1
        else:
            dic[i] = 1
    # print(dic)
    
    key_ = []
    value_ = []
    for k, v in dic.items():
        key_.append(k)
        value_.append(v)
    # print(key_)
    # print(value_)
    if len(key_) == 2 and value_[0] == 2:
        print(f'#{num} Yes')
    else:
        print(f'#{num} No')