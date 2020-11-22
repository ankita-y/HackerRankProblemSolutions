
num = [1,2,3]
def arrayCheck(nums):
    for i in range(len(nums)-1):
        if nums[i] == 1 and nums[i+1] == 2 and nums[i+2] == 3:
            return True
    return False


print(arrayCheck([1,2,1,2,3]))
print(arrayCheck([1,2,2,4,3]))
