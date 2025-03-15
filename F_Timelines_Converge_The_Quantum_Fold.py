import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    results = []

    for _ in range(t):
        n = int(input())
        s = input().strip()

        # Count the number of 0's and 1's
        count_0 = s.count('0')
        count_1 = s.count('1')

        # The minimal length after folding is the maximum of these counts
        min_length = max(count_0, count_1)
        results.append(str(min_length))

    print('\n'.join(results))

if __name__ == "__main__":
    solve()
