t = int(input().strip())
results = []
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().split()))
    a.sort()
    sum_blue, count_blue = 0, 0
    sum_red, count_red = sum(a), n
    for i in range(n - 1):
        sum_blue += a[i]
        count_blue += 1
        sum_red -= a[i]
        count_red -= 1
        if sum_red > sum_blue and count_red < count_blue:
            results.append("YES")
            break
    else:
        results.append("NO")
print("\n".join(results))