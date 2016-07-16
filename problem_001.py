# Project Euler #1: Multiples of 3 and 5
t = int(raw_input())

for _ in xrange(t):
    n = int(raw_input())-1
    x = n/5
    res = ((x*(x+1))/2)*5
    x = n/3
    res += ((x*(x+1))/2)*3
    x = n/15
    res -= ((x*(x+1))/2)*15
    print res