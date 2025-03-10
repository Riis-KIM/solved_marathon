N = int(input())

arr = list(map(int, input().split()))

count = dict()

for item in arr:
    if item in count:
        count[item] += 1
    else:
        count[item] = 1

a = list(count.values())

mx_tmp = max(a)
a.remove(mx_tmp)
sm_tmp = sum(a)

if (mx_tmp - sm_tmp) <= 1:
    print("YES")
else:
    print("NO")
