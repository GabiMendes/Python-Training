# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    # your code
    sheep_count = ""
    i = 1
    
    while i <= n:
        sheep_count += str(i) + " sheep..."
        i += 1
        
    return sheep_count
