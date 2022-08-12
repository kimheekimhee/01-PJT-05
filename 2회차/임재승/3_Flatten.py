import sys

sys.stdin = open("_Flatten.txt")

for i in range(1, 11):
    dump = int(input())
    high = list(map(int, input().split()))
    while dump:
        # 덤프횟수만큼 실행
        dump -= 1
        #제일 높은건 빼주고 작은건 더해주고
        high[high.index(max(high))] -= 1
        high[high.index(min(high))] += 1

    print(f'#{i} {max(high) - min(high)}')
