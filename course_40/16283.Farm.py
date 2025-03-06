# 양 하루 섭취 사료, 염소 하루 섭취 사료, 전체 동물 수, 소비 사료 양
a, b, n, w = map(int, input().split())

count = []
for i in range(1, n):
    if a*i + b*(n-i) == w:
        count.append([i, n-i])

if len(count) == 1:
    print(count[0][0], count[0][1])
else:
    print(-1)