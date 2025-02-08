# test = int(input())
# for _ in range(test):
#     target = list(input().strip())  
#     iter_count = int(input())
    
#     for _ in range(iter_count):
#         i, q = input().split()
#         i = int(i) - 1
#         target[i] = q
              
#         if "1100" in ''.join(target):
#             print("YES")
#         else:
#             print("NO")
# 
test = int(input())
for _ in range(test):
    target = list(input().strip())
    len_target = len(target)
    iter_count = int(input())
    
    count = 0
    for j in range(len_target - 3):
        if target[j] == '1' and target[j+1] == '1' and target[j+2] == '0' and target[j+3] == '0':
            count += 1
    
    for _ in range(iter_count):
        i, q = input().split()
        i = int(i) - 1
        
        original = target[i]
        if original == q:
            print("YES" if count > 0 else "NO")
            continue
        
        for j in range(max(0, i - 3), min(i + 1, len_target - 3)):
            if target[j] == '1' and target[j+1] == '1' and target[j+2] == '0' and target[j+3] == '0':
                count -= 1
        
        target[i] = q
        
        for j in range(max(0, i - 3), min(i + 1, len_target - 3)):
            if target[j] == '1' and target[j+1] == '1' and target[j+2] == '0' and target[j+3] == '0':
                count += 1
        
        print("YES" if count > 0 else "NO")