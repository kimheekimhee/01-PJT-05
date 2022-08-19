import sys

sys.stdin = open("_반반.txt")
T = int(input())
for i in range(1, T+1):
    result = {}
    Text = input()
    for j in Text:
        if j not in result:
            result[j] = 1
        else:
            result[j] += 1
    val = [v for k, v in result.items() if v == 2]
    print(f'#{i}', 'Yes' if len(val) == 2 else 'No')