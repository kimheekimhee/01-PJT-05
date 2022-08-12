import sys

sys.stdin = open("_Flatten.txt")
T = 10
for t in range(1, T+1):
    n = int(input())
    numbers = list(map(int, input().split()))

    for i in range(n):
        numbers[numbers.index(max(numbers))] = numbers[numbers.index(max(numbers))] - 1
        numbers[numbers.index(min(numbers))] = numbers[numbers.index(min(numbers))] + 1

    print(f'#{t} {max(numbers) - min(numbers)}')

    