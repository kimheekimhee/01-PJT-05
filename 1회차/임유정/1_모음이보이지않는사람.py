import sys

sys.stdin = open("_모음이보이지않는사람.txt")

t = int(input())
 
for tc in range(1, t + 1) :
    data = input()
    result = ''
    for i in range(len(data)) :
        if data[i] in ['a', 'e', 'i', 'o', 'u'] :
            continue
        result += data[i]
 
    print('#%d %s' % (tc, result))
