N = int(input())        # 친구 수
M = int(input())        # 게임 횟수
arr = list(map(int, input().split()))       # 각 게임의 타겟

game = [list(map(int, input().split())) for _ in range(M)]      # 각 게임의 진행

score = [0] * N     # 각 사람의 점수 계산

for i in range(M):      # 매 게임의 타겟
    target = arr[i]

    for t in range(N):
        if game[i][t] == target:    # 예상 맞추었다면 사람 점수 +1
            score[t] += 1
        else:               # 예상 못맞추면 타겟 점수 +1
            score[target-1] += 1

# 점수 출력
for k in range(N):
    print(score[k])