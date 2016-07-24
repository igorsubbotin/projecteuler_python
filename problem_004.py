# Project Euler #4: Largest palindrome product
t = int(raw_input())

def is_palindrome(n):
    s = str(n)
    if len(s) != 6:
        return False
    for i in xrange(3):
        if s[i] != s[5-i]:
            return False
    return True

def find_max_palindrome(n):
    global m
    for i in m:
        if i <= n:
            return i
    
m = []
for i in xrange(101, 1000):
    for j in xrange(101, 1000):
        n = i*j
        if is_palindrome(n):
            m.append(n)
m.sort()
m.reverse()
    
for _ in xrange(t):
    n = int(raw_input())
    print find_max_palindrome(n)