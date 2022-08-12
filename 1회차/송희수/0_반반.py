import sys

sys.stdin = open("_반반.txt")

T = int(input())

for tc in range(T):
    word = list(input())
    a = set(word)
    if len(a) != 2:
        print(f"#{tc+1} {'No'}")
    else:
        print(f"#{tc+1} {'Yes'}")