import sys

sys.stdin = open("_반반.txt")

tc = int(input())
strings = []

for i in range(tc):
    strings.append(input())
print(strings, len(strings))


for i in range(len(strings)):
    first_s = []
    second_s = []
    first_s.append(strings[i][0])
    for j in range(1, 4):
        if strings[i][0] == strings[i][j]:
            first_s.append(strings[i][j])
        elif strings[i][0] != strings[i][j]:
            second_s.append(strings[i][j])
    print(first_s)
    print(second_s)
    if len(first_s) == 2 and len(second_s) == 2:
        if first_s[0] == first_s[1] and second_s[0] == second_s[1]:
            print(f'#{i + 1} Yes')
        else:
            print(f'#{i + 1} No')
    else:
        print(f'#{i + 1} No')