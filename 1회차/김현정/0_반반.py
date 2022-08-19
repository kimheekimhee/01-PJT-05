import sys

sys.stdin = open("_반반.txt")

TC = int(input())

for _ in range(1, TC+1):
    S = input()
    S = sorted(S)
    result = ""
    
    if (S[0] == S[1] and S[2] == S[3]):
        if (S[0] == S[1] == S[2] == S[3]):
            result = "No"
        else:
            result = "Yes"
    else:
        result = "No"
    
    print(f"#{_}", result)