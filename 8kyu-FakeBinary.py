# Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.

# Note: input will never be an empty string

def fake_bin(x):
    x = list(x)
    for i in range(len(x)):
        if x[i] < '5':
            x[i] = '0'
        else:
            x[i] = '1'
    return ''.join(x)
