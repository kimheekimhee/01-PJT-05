T = int(input())

for i in range(1, T + 1):
    N = int(input())

    S = input().split()

    ret = []

    # if N % 2:
    #     a = map(lambda x: [i for i in x], zip(S[:N // 2 + N % 2], S[N // 2 + N % 2:]))
    #     for j in a:
    #         ret += j
    # else:
    #     a = map(lambda x: [i for i in x], zip(S[:N // 2], S[N // 2:]))
    #     for j in a:
    #         ret += j

    a = map(lambda x: [i for i in x], zip(S[:N // 2 + N % 2], S[N // 2 + N % 2:]))

    for j in a:
        ret += j

    if N % 2:
        ret += [S[N // 2]]

    print(f"#{i}", *ret)