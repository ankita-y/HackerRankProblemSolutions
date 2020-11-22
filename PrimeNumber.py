import math
n = int(input())
for i in range(n):
    num = int(input())
    if num > 1:
        for j in range(2, int(math.sqrt(num))+1):
            if num % j == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")
