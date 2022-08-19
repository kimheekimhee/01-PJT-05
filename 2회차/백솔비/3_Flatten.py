import sys
sys.stdin = open("_Flatten.txt")

T = 10

for tc in range(1, T+1):
    dump_cnt = int(input())
    land = list(map(int, input().split()))

    for i in range(dump_cnt):
        max_h = max(land)
        min_h = min(land)

        max_i = land.index(max_h)
        min_i = land.index(min_h)

        land[max_i] -= 1
        land[min_i] += 1
    
    print(f'#{tc} {max(land)-min(land)}')
