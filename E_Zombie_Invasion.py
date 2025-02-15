def Zombies(num_zombies,bullet,healths,positions):
    

    while True:
        if all(h<=0 for h in healths):
            return True

        alive_zombies = [(h,p,i) for i,(h,p ) in enumerate(zip(healths,positions)) if h>0]

        if any(abs(p)<=0 for h,p,i in alive_zombies):
            return False
        

    
        for i in range(min(bullet,len(alive_zombies))):
            index = alive_zombies[i][2]
            healths[index] -=1

        
        for i in range(num_zombies):
            if healths[i]>0:
                positions[i] = positions[i]- 1 if positions [i]>0 else positions[i]+1
        





rounds = int(input())
for _ in range(rounds):
    num_zombies,bullet = list(map(int,input().split()))
    healths = list(map(int,input().split()))
    positions = list(map(int,input().split()))
    answer = Zombies(num_zombies,bullet,healths,positions)
    print("YES" if answer else "NO")





















# rounds = int(input())
# for _ in range(rounds):
#     num_zombies,bullet = list(map(int,input().split()))
#     healths = list(map(int,input().split()))
#     positions = list(map(int,input().split()))
#     killed = False
#     combined = sorted(zip(positions,healths),key=lambda x:abs(x[0]))
    
#     if any(p ==0 for p,h in combined):
#         print("NO")
#         killed = True

#     while combined and not killed:
       
#         for _ in range(bullet):
#             if combined:
#                 p,h = combined.pop(0)
#                 h -=1
#                 if h>0:
#                     combined.append((p,h))
#         combined = [(p-1 if p>0 else p+1,h) for p,h in combined ]

#         if any(p ==0 for p,h in combined):
#             print("NO")
#             killed = True
        
#         combined = sorted(combined,key=lambda x:abs(x[0]))    
        
#     if not killed:
#         print("YES")
        

