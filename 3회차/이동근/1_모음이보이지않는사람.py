T = int(input())

open_vowels = list("aeiou")

for i in range(1, T + 1):
    S = input()

    for j in open_vowels:
        S = S.replace(j, '')

    print(f"#{i}", S)