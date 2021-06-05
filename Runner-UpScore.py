if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    mx1 = arr[0]
    mx2 = arr[1]
    for num in arr:
        if num > mx1:
            mx1,mx2 = num,mx1
        elif num > mx2 and num != mx1:
            mx2 = num
        elif mx1 == mx2:
            mx2 = num
            
    # for num in arr:
    #     if num != max(arr) and num > mx1:
    #         mx1 = num
    
    print(mx2)
