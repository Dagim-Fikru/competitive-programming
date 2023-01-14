from math import ceil
arr = list(map(int, input().split()))
m=ceil(arr[0]/arr[2])
n=ceil(arr[1]/arr[2])
flagStone = m*n
print(flagStone)
