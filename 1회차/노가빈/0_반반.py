tc = int(input())
for i in range(tc):
    str = list(input())
    str = set(str)
    if len(str) != 2:
        print(f'#{i+1} No')
    else:
        print(f'#{i+1} Yes')