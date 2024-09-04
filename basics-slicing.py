# INTRO:
# 
# The general syntax is <start>:<stop>:<step> where everything 
# including the : are optional.

# The <start> index indicates beginning index of the slice and 
# <stop> the index at which to stop the slice (that index is 
# excluded in the result). The <step> indicates whether to traverse 
# by stepping over more than one step (the default). 

# For <start> and <stop>, negative values mean the index should be 
# counted from the end rather than the beginning of the collection type. 

# For <step>, negative value means the direction of traversal should be 
# from right to left.

# VANILLA SLICING EXAMPLE
print("VANILLA SLICING EXAMPLE:\n")
l = [2, 7, 9, 10, 1, 0]
print(f"list l: {l}, l[2:5]: {l[2:5]}")
print(
'''\nEXPLANATION: <start> is 2 which is the 3rd element 9, 
<stop> is 5 which is the 6th element 0 (excluded) and 
so the result are the numbers from 9 through 0 in the list but excluding 0.'''
)

# SLICING WITH STEP
print("\nSLICING WITH STEP EXAMPLE:\n")
print(f"list l: {l}, l[2:5:2]: {l[2:5:2]}")
print(
'''\nEXPLANATION: <start> is 2 which is the 3rd element 9, 
<stop> is 5 which is the 6th element 0 (excluded) and so the result 
are the numbers from 9 through 0 in the list but excluding 0 and 
skipping 1 at each step.'''
)

# SLICING WITH NEGATIVE INDEXES
print("\nSLICING WITH NEGATIVE INDEXES EXAMPLE:\n")
print(f"list l: {l}, l[-5:-2]: {l[-5:-2]}")
print(
'''\nEXPLANATION: <start> is -5 which is the 5th element from the right 7, 
<stop> is -2 which is the 2nd  element from the right 1 (excluded) and 
so the result are the numbers from 7 through 1 in the list but excluding 1.

Note 1: For <start> and <stop>, negative values mean the index should be 
counted from the end rather than the beginning of the collection type.

Note 2: If you slice with l[-2:-5], you get the empty list as <start> index is 
greater than the <stop> index.
'''
)

# SLICING WITH NEGATIVE STEP:
print("\nSLICING WITH NEGATIVE STEP EXAMPLE:\n")
print(f"list l: {l}, l[5:2:-1]: {l[5:2:-1]}")
print(
'''\nEXPLANATION: <start> is 5 which is the 6th element 0, 
<stop> is 2 which is the 3rd element 9 (excluded) and 
so the result are the numbers from 0 through 9 in the list but 
excluding 9 and traversing from Right to Left.

Note 1: For <step>, negative value means the direction of 
traversal should be from right to left.

Note 2: If you slice with l[2:5:-1], you get the empty list as 
<start> index is greater than the <stop> index when going from 
Right to Left.
'''
)

# SLICING WITH MISSING INDEXES AND STEP
print("\nSLICING WITH MISSING INDEXES AND STEP EXAMPLE 1:\n")
print(f"list l: {l}, l[:5]: {l[:5]}")
print(
'''\nEXPLANATION: <start> and <step> are missing which means 
we start from the beginning 2 and the step is default (left to 
right, full traversal – no skips). <stop> is 5 which is the 6th 
element 0 (excluded) and so the result are the numbers from 
2 through 0 in the list but excluding 0.

Note: Missing indexes mean slicing from the beginning and/or end 
of the collection depending on the direction indicated by whether 
the step is positive (left to right – default) or negative (right 
to left).
'''
)

print("\nSLICING WITH MISSING INDEXES AND STEP EXAMPLE 2:\n")
print(f"list l: {l}, l[::-1]: {l[::-1]}")
print(
'''\nEXPLANATION: <start> and <stop> are missing and <step> is negative 
which means we start from end and end at the beginning going from 
Right to Left. So, the list will be reversed.

Note: Although slicing can be used as above to reverse or copy lists, 
the recommended way is to use copy.deepcopy instead, to make the intent 
explicit. For shallow copy, there is copy.copy. 
'''
)


