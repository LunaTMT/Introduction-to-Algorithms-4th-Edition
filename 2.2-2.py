"""
 2.2-2
 Page 33
 Introduction to algorithms 4th ed

 Worst case: n^2
 Best case: n^2

The following algorithm only needs to run for n-1 elements for by the time it 
reaches the last element it is alreadt in the correct order. I.e. it is the largest element 
"""

arr = [5, 4, 6, 5, 2, 6]
i = 0
n = len(arr)-1

for i in range(0, n-1):
    lowest = i
    j = i+1
    
    #Finding the smallest element in A[i:n]
    while j <= n:
        if arr[lowest] > arr[j]:
            lowest = j
        j+=1 
    arr[i], arr[lowest] = arr[lowest], arr[i]

print(arr)
