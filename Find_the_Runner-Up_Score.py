if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    print(arr)
    maximum = max(arr)
    while maximum in arr:
        arr.remove(maximum)
    
    print(max(arr))
    