import sys

sys.stdin = open("_Flatten.txt")

for test_case in range(1, 10 + 1):
    n = int(input())
    list_ = list(map(int, input().split()))
    for i in range(n):
        max_n = max(list_)
        min_n = min(list_)
        max_index = list_.index(max_n)
        min_index = list_.index(min_n)
        list_[max_index] -= 1
        list_[min_index] += 1
    print(f'#{test_case} {max(list_) - min(list_)}')