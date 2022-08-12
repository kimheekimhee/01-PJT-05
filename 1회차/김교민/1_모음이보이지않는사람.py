from dataclasses import replace
import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t=int(input())
mo=['a','e','i','o','u']
for case in range(1, t+1):
    munja = input()
    re = ''
    for i in munja:
        if i not in mo:
            re += i
    print(f'#{case} {re}')