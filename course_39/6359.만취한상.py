# 지수의 개수를 구하는 함수
def count_divide(N):
    count = 0
    for i in range(1, int(N**0.5) + 1):
        if N%i == 0:
            if i != N//i:
                count += 2
            else:
                count += 1

    return count

# 테스트 케이스 개수
T = int(input())

for test_case in range(T):
    room = int(input())     # 방 개수
    run_prison = 0          # 도망간 죄수

    for i in range(1, room+1):      # 죄수가 속한 방 숫자의 지수 개수가 홀수면 도망감
        if count_divide(i) % 2 != 0:
            run_prison+= 1

    print(run_prison)

