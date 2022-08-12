
tc = int(input())
for i in range(tc):
    str = input()
    str = str.replace('a','')
    str = str.replace('e','')
    str = str.replace('i','')
    str = str.replace('o','')
    str = str.replace('u','')
    print(f'#{i+1} {str}')