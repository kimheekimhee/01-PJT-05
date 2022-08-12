import sys

sys.stdin = open("_Flatten.txt")
T = 10
for i in range(1, T+1):
    shake = int(input())
    number = list(map(int, input().split()))
    for j in range(shake):
        number.sort()
        number0 = number.pop(0) + 1; number99 = number.pop() - 1
        number.append(number0); number.append(number99)
    chai = max(number) - min(number)
    print(f'#{i}', chai)
