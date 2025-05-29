from itertools import permutations

def print_permutations(s):
    for perm in permutations(s):
        print(perm)
        #print("".join(perm))#Since perm is a tuple of characters (e.g., ('A', 'B', 'C')), we use "".join(perm) to convert the tuple into a string before printing.

print(print_permutations("ADC"))

#The function generates all N! permutations.
# TC = O(N!)