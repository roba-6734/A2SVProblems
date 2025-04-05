def max_blocks(heights):
    n = len(heights)
    sorted_heights = sorted(heights)
    
    max_h = 0  # Current maximum height in original array
    blocks = 0
    
    for i in range(n):
        max_h = max(max_h, heights[i])
        
        # If the max height we've seen so far equals the element at this position in the sorted array,
        # we can end a block here
        if max_h == sorted_heights[i]:
            blocks += 1
    
    return blocks

# Testing with example cases
test1 = [1, 2, 3]
print(max_blocks(test1))  # Expected: 3

test2 = [2, 1, 3, 2]
print(max_blocks(test2))  # Expected: 2