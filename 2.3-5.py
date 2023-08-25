def insertionSortRecusive(arr, n):
    if n <= 1:
        return
    
    insertionSortRecusive(arr, n-1)

    last = arr[n-1]
    j = n-2

    while j >= 0 and arr[j] > last:
        arr[j + 1] = arr[j]
        j -= 1

    arr[j+1] = last

arr = [4,6,2,8,3]
insertionSortRecusive(arr, len(arr))
print(arr)
