# I = 2126 R + 7152 G + 722 B

# 변환식에 따라 알맞는 아스키코드 문양을 반환
def change_to_ascii(R, G, B):
    intensity = (R * 2126) + (G * 7152) + (B * 722)
    if 0<=intensity<510000:
        return '#'
    elif 510000<=intensity<1020000:
        return 'o'
    elif 1020000<=intensity<1530000:
        return '+'
    elif 1530000<=intensity<2040000:
        return '-'
    else:
        return '.'


N, M = map(int, input().split())

picture = [list(map(int, input().split())) for _ in range(N)]

ascii_art = [[None] * M for _ in range(N)]

# 아스키 코드 변환 수행
for i in range(N):
    for j in range(M):
        ascii_art[i][j] = change_to_ascii(picture[i][j*3], picture[i][j*3+1], picture[i][j*3+2])

# 아스키 코드 출력
for i in range(N):
    print(''.join(ascii_art[i]))
