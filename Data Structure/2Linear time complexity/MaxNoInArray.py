arr = [3,46,7,88,5,44,7,87]

def find_max(array):

    max_val = array[0]

    for i in array:
        if i > max_val:
            max_val = i
    print(f'The maximum value in the array is {max_val}')

find_max(arr)

#function loops through n elements once 
#this function has O(n) time complexity
    

