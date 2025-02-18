messages = int(input())
store = [input() for _ in range(messages)]

seen = set()  
for i in range(messages - 1, -1, -1): 
    if store[i] not in seen:
        seen.add(store[i])
        print(store[i])
