import sys

sys.stdin = open("_모음이보이지않는사람.txt")
T = int(input())
for i in range(1, T+1):
    Text = input()
    result = []
    for j in Text:
        if j not in 'aeiou':
            result.append(j)
    print(f'#{i}', ''.join(result))