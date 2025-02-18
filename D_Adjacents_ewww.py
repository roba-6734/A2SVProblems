def Adjacent(n):      
        if n ==1:
            print(1)
            return
        if n ==2:
            print(-1)
            return
        matrix = [[0] * n for i in range(n)]
        nums = list(range(1,n*n+1,2)) + list(range(2,n*n+1,2))

        index =0
        
        for r in range(n):
            for c in range(n):
                matrix[r][c] = nums[index]
                index +=1

        for r in range(len(matrix)):
            for c in range(len(matrix[r])):
                print(matrix[r][c],end=' ')
            print()

rounds  = int(input())
for _ in range(rounds):
    n = int(input())
    Adjacent(n)
