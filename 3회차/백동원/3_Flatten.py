import sys

sys.stdin = open("_Flatten.txt")
for _ in range(1, 11):
    trying = int(input())
    numbers = list(map(int, input().split()))
    for a in range(trying):
        numbers[numbers.index(max(numbers))] -= 1
        numbers[numbers.index(min(numbers))] += 1
    result = max(numbers) - min(numbers)
    print(f'#{_} {result}')