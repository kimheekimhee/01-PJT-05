import sys

sys.stdin = open("_반반.txt")

tc = int(input())



for t in range(tc):
    alphabet = input()
    dict_ = {}
    key = []
    value = []
    for i in alphabet:
        dict_[i] = 0
    for j in alphabet:
        dict_[j] += 1

    for k, v in dict_.items():
        key.append(k)
        value.append(v)
    if len(key) == 2 and len(value) == 2:
        print(f'#{t+1} Yes')
    else:
        print(f'#{t+1} No')