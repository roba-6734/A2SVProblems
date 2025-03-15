n, t = list(map(int,input().split()))
arr = list(map(int,input().split()))

start = 0
current_sum = 0
max_count = 0

for end in range(n):
    current_sum += arr[end]

    while current_sum > t:
        current_sum -= arr[start]
        start += 1

    max_count = max(max_count, end - start + 1)


print(max_count)

