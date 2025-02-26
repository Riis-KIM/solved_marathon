N = int(input())

dot = [list(map(int, input().split())) for _ in range(N)]

dot.sort()  # 가로 길이
x = dot[-1][0] - dot[0][0]

dot.sort(key=lambda x:x[1])     # 세로 길이
y = dot[-1][1] - dot[0][1]

print(x*y)