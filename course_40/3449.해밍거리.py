T = int(input())

for _ in range(T):
    a = input()
    b = input()

    ham = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ham += 1

    print(f"Hamming distance is {ham}.")