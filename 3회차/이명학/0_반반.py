import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-05\\3회차\\이명학\\_반반.txt")

TC = int(input())

for _ in range(1, TC+1):
    list_ = list(map(str, input()))
    # list_ = ['A', 'B', 'A', 'B']
    list_ = sorted(list_)
    # list_ ['A', 'A', 'B', 'B']
    # 길이가 4이므로 정렬했을 때 1번째 글자와 3번째, 4번째가 같지 않으면 Yes
    if list_[0] == list_[1] and (list_[0] != list_[2] or list_[0] != list_[3]) and list_[2] == list_[3]:
        print(f"#{_} Yes")
    else:
        print(f"#{_} No")
