import sys

sys.stdin = open("_Flatten.txt")

for test in range(1, 11):
    cnt = int(input())
    numbers = list(map(int, input().split()))

    while cnt != 0:
        b = max(numbers)
        s = min(numbers)
        numbers[numbers.index(b)] -= 1
        numbers[numbers.index(s)] += 1
        cnt -= 1
    print(f'#{test} {max(numbers) - min(numbers)}')