import sys

sys.stdin = open("_반반.txt")

T = int(input())

for i in range(T):
    string = input()

    check = dict()
    for j in string:
        if j in check:
            check[j] += 1
        else:
            check[j] = 1
    
    final_check = 0
    for _ in check:
        if check[_] != 2:
            final_check = 1

    if final_check == 0:
        print(f'#{i + 1}', 'Yes')
    else:
        print(f'#{i + 1}', 'No')