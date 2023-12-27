# Complete the solution so that it reverses the string passed into it.

# 'world'  =>  'dlrow'
# 'word'   =>  'drow'

def solution(string):
    string_aux = ''
    i = len(string) - 1
    
    while i >= 0:
        string_aux += string[i]
        i -= 1
        
    return string_aux
