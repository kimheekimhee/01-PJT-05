import sys

sys.stdin = open("_Flatten.txt")

T = 10

result = []
for tc in range(1, T + 1):
    dump = int(input())
    box = list(map(int, input().split()))

    for i in range(dump):
        box.sort()
        box[0] += 1
        box[-1] -= 1
    
    box.sort()
    result.append(box[-1] - box[0])

    print(f'#{tc}', result[0])
    del result[0]