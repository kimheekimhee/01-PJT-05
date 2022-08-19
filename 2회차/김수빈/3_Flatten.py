import sys
sys.stdin = open("_Flatten.txt")

for i in range(1, 11):
    d = int(input())
    box = list(map(int, input().split()))
    for j in range(d):
        box[box.index(max(box))] -= 1   # 최대 박스 수 -1
        box[box.index(min(box))] += 1   # 최소 박스 수 +1        
        if max(box) - min(box) < 2:
            break
    print(f'#{i} {max(box) - min(box)}')
