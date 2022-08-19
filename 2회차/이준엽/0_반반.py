import sys

sys.stdin = open("_반반.txt")

tc = int(input())
for i in range(1,tc+1):
    word = input()
    setword = set(list(word))
    if len(setword) == 2:
        if word.count(list(setword)[0]) == 2:
            answer = 'Yes'
        else:
            anser = 'No'
    else:
        answer = 'No'
    print(f'#{i} {answer}')
    