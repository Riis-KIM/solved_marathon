def check(a, b, n):
    for t in range(n):
        if A[a][t] == 1 and B[t][b] == 1:
            return True

    return False

N = int(input())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]

cnt = 0
for i in range(N):
    for j in range(N):
        if check(i, j, N):
            cnt += 1

print(cnt)