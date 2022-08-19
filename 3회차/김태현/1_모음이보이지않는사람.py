import sys
sys.stdin = open("_모음이보이지않는사람.txt")

# 모음 리스트를 만들고
# 반복문 돌면서 모음 리스트에 해당 되지 않을 때만 result.append()

vowels = "aeiou"

T = int(input())

for t in range(1, T+1):
    
    result = []
    word = input()

    for i in word:
        if i not in vowels:
            result.append(i)

    print(f"#{t}", end=" ")
    print(*result, sep="")