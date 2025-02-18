def min_swaps_to_beautiful_tree(n, p):
    def dfs(l, r):
        if l == r:
            return 0, [p[l]]
        
        mid = (l + r) // 2
        left_swaps, left_seq = dfs(l, mid)
        right_swaps, right_seq = dfs(mid + 1, r)
        
        if left_seq == sorted(left_seq) and right_seq == sorted(right_seq):
            if left_seq[-1] < right_seq[0]:
                return left_swaps + right_swaps, left_seq + right_seq
            elif right_seq[-1] < left_seq[0]:
                return left_swaps + right_swaps + 1, right_seq + left_seq
        
        return float('inf'), []
    
    swaps, sequence = dfs(0, len(p) - 1)
    return swaps if swaps != float('inf') else -1

# Reading input
import sys
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1
results = []

for _ in range(t):
    m = int(data[index])
    p = list(map(int, data[index + 1:index + 1 + m]))
    index += 1 + m
    n = m.bit_length() - 1
    result = min_swaps_to_beautiful_tree(n, p)
    results.append(result)

# Printing results
for res in results:
    print(res)
