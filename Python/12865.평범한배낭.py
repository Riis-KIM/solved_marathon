# 물건의 수(N)와 최대 무게(K) 입력 받기
N, K = map(int, input().split())

# 각 물건의 무게와 가치 입력 받기
stuff = [list(map(int, input().split())) for _ in range(N)]

# DP 테이블 초기화: bag[i][w]는 i번째 물건까지 고려하고 무게 w일 때의 최대 가치
bag = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

# DP 계산
for i in range(1, N + 1):
    for w in range(1, K + 1):
        weight, value = stuff[i-1]  # 현재 물건의 무게와 가치
        if weight > w:
            # 현재 물건이 너무 무거워 넣을 수 없는 경우
            bag[i][w] = bag[i-1][w]
        else:
            # 현재 물건을 넣는 경우와 넣지 않는 경우 중 최대 가치 선택
            bag[i][w] = max(bag[i-1][w], bag[i-1][w-weight] + value)

# 모든 물건을 고려했을 때의 최대 가치 출력
print(bag[N][K])