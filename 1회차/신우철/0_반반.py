import sys

sys.stdin = open("_반반.txt")
t = int(input())
for test in range(1,t+1):
    a = input()
    count_ = 0
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j]:
                count_ += 1
            
    if count_ == 8:
        print(f'#{test} Yes')
    else:
        print(f'#{test} No')