t = int(input())
for _ in range(t):
    n, m, k = map(int, input().split())
    a = sorted(input().strip())
    b = sorted(input().strip())

    result = []
    count_a = count_b = 0

    while a and b:
        if (a[0] < b[0] and count_a < k) or count_b == k:
            result.append(a.pop(0))
            count_a += 1
            count_b = 0
        else:
            result.append(b.pop(0))
            count_b += 1
            count_a = 0

    print(''.join(result))