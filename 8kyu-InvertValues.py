# Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.

# invert([1,2,3,4,5]) == [-1,-2,-3,-4,-5]
# invert([1,-2,3,-4,5]) == [-1,2,-3,4,-5]
# invert([]) == []

# You can assume that all values are integers. 
#>>Do not mutate the input array/list.<<

def invert(lst):
    lst_copy = lst.copy()
    position = 0
    while position < len(lst_copy):
        lst_copy[position] = -(lst_copy[position])
        position += 1
    return lst_copy
