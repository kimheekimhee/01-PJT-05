import sys

sys.stdin = open("_Flatten.txt")

# 풀다가 막힌 문제
T = 10
for tc in range(1, T+1):
    number = int(input())
    height = list(map(int, input().split()))
    max_height = max(height) # 최고점
    min_height = min(height) # 최저점