from math import log2

"""
suppose insertion sort uns at 8n^2 and,
merge sort runs in 64n lg n 
For which values of n does insertion sort beat merge sort
"""

def merge_sort(n):
    return int(64*n * log2(n))

def insertion_sort(n):
    return 8 * (n ** 2)

n = 2
m = merge_sort(n)
i = insertion_sort(n)

while not (i > m):
    m = merge_sort(n)
    i = insertion_sort(n)
    print(f"""
          N : {n}
          Merge Sort : {m}, 
          Insertion Sort : {i} 
          Insertion > Merge : {i > m}
          """)
    n += 1
print(f"Thus Insertion sort beats merge sort in this instance when n = {n-1}")

"""
Exercise 1.2-2
We wish to determine for which values of n the inequality 
8n^2 < 64n log2(n) holds. 

This happens when n < 8 log2(n), or when n ≤ 43. 

In other words,
insertion sort runs faster when we’re sorting at most 43 items. Otherwise merge
sort is faster.
"""
