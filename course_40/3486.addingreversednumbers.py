N = int(input())

for _ in range(N):
    a, b = input().split()

    tmp_a = ''
    tmp_b = ''
    for i in range(1, len(a)+1):
        tmp_a += a[-i]
    for i in range(1, len(b)+1):
        tmp_b += b[-i]

    tmp_c = int(tmp_a) + int(tmp_b)

    print(int(str(tmp_c)[::-1]))