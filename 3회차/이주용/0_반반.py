import sys

sys.stdin = open("_반반.txt")
t = int(input())
for i in range(1, t + 1):
    s = list(input())
    s_dict = {}
    for letter in s:
        if letter not in s_dict:
            s_dict[letter] = 1
        else:
            s_dict[letter] += 1
    if list(s_dict.values()) == [2, 2]:
        print('#{}'.format(i), 'Yes')
    else:
        print('#{}'.format(i), 'No')
        
    