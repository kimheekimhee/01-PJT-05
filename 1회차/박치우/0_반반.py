import sys

sys.stdin = open("_반반.txt")
test_case = int(input())


for i in range(test_case):
    dic = dict()
    word = input()
    for j in word:
        if j not in dic:
            dic[j] = 1
        else:
            dic[j] +=1
    if len(dic) == 2:
        print('Yes')
    else:
        print('No')
    