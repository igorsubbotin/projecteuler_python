# Project Euler #6: Sum square difference
import math

def sum_of_squares(n):
    res = 1
    for i in xrange(2, n+1):
        res += i**2
    return res

def square_of_sum(n):
    res = 0
    for i in xrange(1, n+1):
        res += i
    return res**2

t = int(raw_input())
for _ in xrange(t):
    n = int(raw_input())
    print abs(sum_of_squares(n) - square_of_sum(n))