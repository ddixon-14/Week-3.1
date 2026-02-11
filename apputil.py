import seaborn as sns
import pandas as pd


"""Fib(n) returns the n'th number of the Fibonacci series"""
def fib(n):
    if n == 0: #base case
        return 0
    elif n == 1: #base case
        return 1
    else:
        return fib(n-1) + fib(n-2) #recursive case
    
print(fib(10)) 


