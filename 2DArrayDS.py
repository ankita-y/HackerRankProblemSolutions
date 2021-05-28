import math
import os
import random
import re
import sys

def hourglassSum(arr):
  l = []
  for i in range(4):
    for j in range(4):
      sum = 0
      # Top
      sum += arr[i][j] + arr[i][j+1] + arr[i][j+2]
      # Middle
      sum += arr[i+1][j+1]
      # Bottom
      sum += arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
      l.append(sum)
      
   return max(l)

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'],'w')
  arr = []
  for _ in range(6):
    arr.append(list(map(int,input().rstrip().split())))
  result = hourglass(arr)
  
  fptr.write(str(result) + '\n')
  fptr.close()
