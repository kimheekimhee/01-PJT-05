import sys
# card = input()

small_result = []
big_result = []
result = []


for _ in range(1):
    card_num = int(input())
    vowel = list(map(str,input().split()))
    for i in range(card_num):
        if i >= card_num/2:
            big_result.append(vowel[i])
        if i < card_num/2:
            small_result.append(vowel[i])
    for j in range(round(card_num/2)):
        result.append(small_result[j])
        result.append(big_result[j])


print(*result)


sys.stdin = open("_퍼펙트셔플.txt")

