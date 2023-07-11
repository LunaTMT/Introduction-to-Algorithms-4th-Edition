#2.2-2
# Page 33
#introduction to algorithms 4th ed

#worst case: n^2
#best case: n^2

arr = [5, 4, 6, 5, 2, 6]
i = 0
n = len(arr)-1

for i in range(0, n-1):
    min_idx = i
    j = i+1
    
    while j <= n:
        if arr[min_idx] > arr[j]:
            min_idx = j
 
        j+=1 
    arr[i], arr[min_idx] = arr[min_idx], arr[i]

print(arr)
