import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())
result = []

for _ in range(1, T+1):
    alpha = input()
    alpha_re = ""

    for i in alpha:
        if i in 'aeiou':
            alpha = alpha.replace(i, '')
    
    print(f"#{_}", alpha)