import sys

sys.stdin = open("_모음이보이지않는사람.txt")

# t = int(input())

# for tc in range(1, t+1):
#     data = input()
#     result = " "
#     for i in range(len(data)):
#         if data[1] in ['a', 'e', 'i', 'o', 'u']:
#             continue
#         result += data[i]

#     print('#%d %s' % (tc, result))


T = int(input())
 
for tc in range(1,1+T):
    word = str(input())
    my_word = ''
 
    for q in word:
        
        if q != 'a' and q != 'e' and q != 'i' and q != 'o' and q != 'u':
            my_word += q
 
    print('#{} {}'.format(tc,my_word))