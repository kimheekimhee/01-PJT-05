# 주어진 단어를 어떻게 인식하는지를 출력한다.

import sys

sys.stdin = open("_모음이보이지않는사람.txt")

T = int(input())

# 모음 목록
c = ['a','i','u','o','e']

for t in range(1,T+1):
    s = input()
    s.lower()
    # 단어에서 모음을 제거한다.
    for i in c:
        s = s.replace(i,'')
    print(f"#{t} {s}")