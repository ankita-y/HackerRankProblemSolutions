# Two or more arrays can be concatenated together using the concatenate function with a tuple of the arrays to be joined:
import numpy as np

n,m,p = map(int,input().split())
L1 = []
L2 = []
for i in range(n):
    a = []
    a = list(int(j) for j in input().split())
    L1.append(a)
for i in range(m):
    a = []
    a = list(int(j) for j in input().split())
    L2.append(a)

print(L1)
arr1 = np.array(L1)
arr2 = np.array(L2)
print(np.concatenate((arr1,arr2)))

# Sample Input
# 4 3 2
# 1 2
# 1 2 
# 1 2
# 1 2
# 3 4
# 3 4
# 3 4 

# Sample Output
# [[1 2]
#  [1 2]
#  [1 2]
#  [1 2]
#  [3 4]
#  [3 4]
#  [3 4]] 
