import sys

sys.stdin = open("test.txt")

a, b = map(int, input().split())

print(a - b)