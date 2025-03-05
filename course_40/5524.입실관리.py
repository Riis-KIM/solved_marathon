N = int(input())

arr = [list(input().split()) for _ in range(N)]

for i in range(N):
    a = arr[i]
    a = [word.lower() for word in a]
    print(a[0])

