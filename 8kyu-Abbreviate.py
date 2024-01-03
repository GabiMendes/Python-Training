# Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

# It should look like this:
# Sam Harris => S.H

def abbrev_name(name):
    names = name.split()
    initials = names[0][0].upper() + "." + names[1][0].upper()
    return initials
