# import sys

# sys.stdin = open("_반반.txt")


TC = int(input())

for i in range(1, TC+1):
    str_ = input()
    if len(set(str_)) == 2:
        for j in str_[1]:
            str_.count(j) == 2
            print(f'#{i} Yes')
    else: 
        print(f'#{i} No')