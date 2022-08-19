import sys

sys.stdin = open("_반반.txt")

N = int(input())

for j in range(1, N+1):
  
    T = input()
    for i in T:
        # print(i)
        if T.count(i) == 2:
            a = 'Yes'
        else:
            a = 'No'
            break

    print(f'#{j} {a}')


