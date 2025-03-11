from collections import deque

def check():
    mx_cnt = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                return(-1)
            elif box[i][j] > mx_cnt:
                mx_cnt = box[i][j]

    return mx_cnt


M, N = map(int, input().split())

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

box = [list(map(int, input().split())) for _ in range(N)]

q = deque()
check_cnt = 0

for i in range(N):
    for j in range(M):

        if box[i][j] == 0:
            check_cnt += 1

        elif box[i][j] == 1:
            q.append([i, j, 0])


while q and check_cnt >= 1:
    ni, nj, cnt = q.popleft()
    for k in range(4):
        ti, tj = ni + dy[k], nj + dx[k]
        if 0<=ti<N and 0<=tj<M and box[ti][tj] == 0:
            box[ti][tj] = cnt + 1
            q.append([ti, tj, cnt+1])

mxcnt = 0
if check_cnt != 0:
    mxcnt = check()

print(mxcnt)
