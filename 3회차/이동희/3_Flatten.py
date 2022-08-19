import sys

sys.stdin = open("_Flatten.txt")

for tc in range(1, 11):
    dump_cnt = int(input())
    storage = list(map(int, input().split()))
    
    while dump_cnt > 0:
        storage[storage.index(min(storage))] += 1
        storage[storage.index(max(storage))] -= 1
        dump_cnt -= 1
        
    print(f'#{tc} {abs(max(storage) - min(storage))}')