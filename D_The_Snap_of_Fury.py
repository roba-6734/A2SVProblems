n = int(input())
L = list(map(int, input().split()))


diff = [0] * (n + 1)

for i in range(n):
    if L[i] > 0:
        start = max(0, i - L[i])
        diff[start] += 1
        diff[i] -= 1  

print(diff)
destroyed = [0] * n
current = 0
for i in range(n):
    current += diff[i]
    destroyed[i] = current > 0  


survivors = destroyed.count(False)
print(survivors)