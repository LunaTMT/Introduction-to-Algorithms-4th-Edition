# 2.1-4
# Page 25
# introduction to algorithms 4th ed

arr = [1, 2, 3, 4, 5]
target = 5
i = 0
n = len(arr)
while i < n-1 and arr[i] != target:
    i += 1

print(f"{f'Index : {i}' if arr[i] == target else None}")
