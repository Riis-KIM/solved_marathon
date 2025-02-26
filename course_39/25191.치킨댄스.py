KFC = int(input())
cola, beer = map(int, input().split())

total_chicken = cola//2 + beer

if KFC > total_chicken:
    print(total_chicken)
else:
    print(KFC)