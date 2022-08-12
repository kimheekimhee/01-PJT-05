import sys

sys.stdin = open("_반반.txt")

# 길이 4의 알파벳 대문자로 이루어진 문자열 S가 주어졌을 때,
# S에 정확히 두 개의 서로 다른 문자가 등장하고,
# 각 문자가 정확히 두 번 등장하는 지 판별하라.

word_li = []
for t in range(1,1+int(input())):
    word = input()
    word_li.append(word)
# print(word_li)


    for i in range(len(word_li)):
        dic={}
    
        for w in word_li[i]:
            # print(w) 요소 하나 씩
            dic[w]=dic.get(w,0)+1
        ans = 'Yes'
        for v in dic.values():
            if v != 2:
                ans = 'No'
                break
    print(f'#{t} {ans}')
