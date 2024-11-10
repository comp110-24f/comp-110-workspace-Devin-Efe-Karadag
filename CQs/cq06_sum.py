"""Summing the elements of a list using different loops"""
__author__ = "730813763"


def w_sum(vals: list[float]) -> float:
    i: int = 0 # For getting the values at index i
    sum: float = 0.0 # to sum up the values in each iteration
    while i < len(vals):
        sum += vals[i]
        i+=1
    return sum 


def f_sum(vals: list[float]) -> float:
    sum: float = 0.0 # to sum up the values in each iteration
    for num in vals: # no need for an index variable in for in loop without range
        sum+= num
    return sum

def f_range_sum(vals: list[float]) -> float:
    i: int = 0 # For getting the values at index i 
    sum: float = 0.0 # to sum up the values in each iteration
    for i in range(len(vals)):
        sum += vals[i]
    return sum
