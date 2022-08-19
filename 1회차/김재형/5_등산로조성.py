import sys
sys.stdin = open("_등산로조성.txt")
from pprint import pprint

# 등산로 시작은 가장 높은 봉우리
# 낮은 숫자로만 이동 가능
# 딱 한 곳을 k만큼 팔 수 있음

T = int(input())

for t in range(T):
    n, k = map(int, input().split())
    m_map = [list(map(int, input().split())) for _ in range(n)]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 0, 1, -1]
    
    x = 0
    y = 0
    max_ = []
    
    for i in range(n):
        m = len(m_map[i])
        for j in range(m):
            # 최대값 얼만지 구하기
            if m_map[i][j] == max(m_map[i]):
                max_.append(m_map[i][j])
            # 델타 탐색
            for q in range(4):
                nx = x + dx[q]
                ny = y + dy[q]
            
                if -1 < nx < n and -1 < ny < n:
                    