import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

N = ['a','e','i','o','u']

for tc in range(T):
    w = input()
    w = list(w)
    li = []
    for i in w:
        if i not in N:
            li.append(i)
    print(f"#{tc+1} {''.join(li)}")