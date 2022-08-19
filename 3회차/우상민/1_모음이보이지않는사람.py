import sys

sys.stdin = open("_모음이보이지않는사람.txt")

for TC in range(1, int(input())+1):
    N = input().replace('a', '').replace('e', '').replace('i', '').replace('o', '').replace('u', '')
    print(f'#{TC}', N)
