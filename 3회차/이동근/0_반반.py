T = int(input())

for i in range(1, T + 1):
    S = input()

    d = {}

    for alpha in S:
        if alpha not in d:
            d[alpha] = 1
        else:
            d[alpha] += 1

    print(f"#{i}", "Yes" if len(d) == 2 and [2, 2] == list(d.values()) else "No")