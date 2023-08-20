
"""
What is smallest value of n such that A1 runs faster than A2
A1 = 100n^2
A2 = 2^n
"""

def A1(n):
    return 100 * (n ** 2)

def A2(n):
    return 2 ** n

n = 1
a1 = A1(n)
a2 = A2(n)

while not (a1 < a2):
    a1 = A1(n)
    a2 = A2(n)
    print(f"""
          N : {n}
          A1: {a1}, 
          A2 : {a2} 
          A1 < A2 : {a1 < a2}
          """)
    n += 1
print(f"Thus, the smallest value for n such that A1 runs faster than A2 is {n-1}")
