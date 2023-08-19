from math import log, e

"""
suppose insertion sort uns at 8n^2 and,
merge sort runs in 64n lg n 
For which values of n does insertion sort beat merge sort
"""

def merge_sort(n):
    return int(64*n * log(e) )

def insertion_sort(n):
    return 8 * (n ** 2)

n = 0
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
print(f"Thus Insertion sort beats merge sort in this instance when n = {n}")