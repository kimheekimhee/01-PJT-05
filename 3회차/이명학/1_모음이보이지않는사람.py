import sys

sys.stdin = open(
    "C:\\Users\\이명학\\Desktop\\멀티캠퍼스\\01-PJT-05\\3회차\\이명학\\_모음이보이지않는사람.txt")


T = int(input())

alpha_list = ['a', 'e', 'i', 'o', 'u']

for _ in range(1, T+1):
    word_list = list(map(str, input()))
    # word_list = ['c', 'o', 'n', 'g', 'r', 'a', 't', 'u', 'l', 'a', 't', 'i', 'o', 'n']
    removed_list = [i for i in word_list if i not in alpha_list]  # 중복값 제거
    result = "".join(removed_list)  # f-string을 쓰기위해 result에 할당
    print(f"#{_} {result}")
