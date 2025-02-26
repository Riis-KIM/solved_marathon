N = int(input())        # 단어 길이

word = list(input())    # 단어

for i in range(len(word)//2 + 1):   # 단어 전체의 절반에 대해서 확인
    if word[i] == '?':              # 단어가 ? 일때
        if word[-i-1] == '?':         # 반대쪽 단어도 ? 면
            word[i], word[-i-1] = 'a', 'a'        # 'a'로 둘 다 바꿈
        else:
            word[i] = word[-i-1]      # 반대쪽 단어는 ?가 아니라면
    elif word[-i-1] == '?':           # 반대쪽 단어가 ? 라면
        word[-i-1] = word[i]

print(''.join(word))
