"""
Everything can be worked out in relation to n = 1*10^6 for one second as a ratio
        lg(n): 2 ^ n
           √n: n ^ 2 
            n: 1 * 10^6
      n lg(n): (2 ^ n) / n
          n^2: n ^ 1/2
          n^3: n ^ 1/4
          2^n: log2(n)

I do not see how this could be done factorially however.
Thus the factorial function will have to be done using a counter
"""

from math import factorial, log, log2
import csv


def generate_times():
    second = 1000000
    minute = 60 * second
    hour = 60 * minute
    day = 24 * hour
    month = 30 * day
    year = 365 * day
    century = 100 * year
    return [second, minute, hour, day, month, year, century]

def lg_n(n):
    return f"2^{n}"


def square_root_n(n):
    return n ** 2 

def n(n):
    return n

"""
Following two functions copied from https://donrwalsh.github.io/CLRS/solutions/01/p1-1
"""
def n_lg_n(time):
    time_taken, n = 0, 0
    initial_n = 1
    # overshoot the first n
    while time_taken <= time:
        initial_n *= 10
        time_taken = (initial_n * log(initial_n, 2))
    # now double back iteratively and determine the specific location
    n = 0
    for x in range(len(str(initial_n))):
        o = initial_n // 10 ** x
        n = n_lg_n_helper(time, o, n)
    return n

def n_lg_n_helper(time, o, n_so_far):
    time_taken = 0  
    n = n_so_far
    while time_taken < time:
        n += o
        time_taken = (n * log(n, 2))
    return n - o

def n_power_2(n):
    return int(n ** 0.5)

def n_power_3(n):
    return int(n ** 0.25)

def two_power_n(n):
    return int(log2(n))

#Following function copied from https://donrwalsh.github.io/CLRS/solutions/01/p1-1
def n_factorial(time):
    time_taken, n = 0, 0
    while time_taken <= time:
        n += 1
        time_taken = factorial(n)
    return n-1



times = generate_times()
excel_column_headers = ["functions", "second", "minute", "hour", "day", "month", "year", "century"]

functions = (lg_n, square_root_n, n , n_lg_n, n_power_2, n_power_3, two_power_n, n_factorial)

values = {  "lg(n)"    : [],
               "√n"    : [],
                "n"    : [],
          "n lg(n)"    : [],
              "n^2"    : [],
              "n^3"    : [],
              "2^n"    : [],
               "n!"    : []}


for function, key in zip(functions, values.keys()):
    for time in times:
        values[key].append(str(function(time)))


with open("table.csv", mode='w', newline='') as file:
    
    writer = csv.writer(file)
    center_aligned_row = [cell.center(15) for cell in excel_column_headers]
    writer.writerow(center_aligned_row)

    for key, value in values.items():
        row = [key] + value
        right_aligned_row = [cell.rjust(15) for cell in row]  
        writer.writerow(right_aligned_row)
