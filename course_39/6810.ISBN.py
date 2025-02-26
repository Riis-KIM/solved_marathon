N = 9780921418000

N += (int(input()) * 100)
N += (int(input()) * 10)
N += (int(input()))

N = str(N)
total = 0
for i in range(13):
    if i % 2 == 0:     # 짝수일때
        total += int(N[i])
    else:
        total += int(N[i]) * 3

print("The 1-3-sum is", total)
