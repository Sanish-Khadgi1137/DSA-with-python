# "lst" must be in ascending order

def binary_search(lst, num):
    #initializing lower and upper bounds
    l = 0  # index
    u = len(lst) -  1 #in py index start with 0 so, if len = 6 then index of last element is  6-1=5

   #index
    while l <= u:  # even l = u; this while should run
        mid = (l + u) // 2  # "//" for integer division

        #element
        if lst[mid] == num:
            # globals()['pos'] = mid #globals variable which is available outside of this function too
            return mid + 1 #position(no python index)

        else:
            if lst[mid] < num:
                l = mid+1 #to avoid potential (position last or not in the list) infinite loop(we could get same mid again and again due to integer division) we use "+1"
            else:
                u = mid-1 #to avoid potential (position last or not in the list) infinite loop we use "-1"

    return None  # if not found


lsta = [1, 3, 5, 7, 9, 12, 55, 56]
num1 = 55

position = binary_search(lsta, num1)

if position:
    print(position)
else:
    print("Not found")


# if binary_search(lsta, num1):
#     print('found at', pos+1)
# else:
#     print("Not found")

#IN binary search each iteration reduces search space by half
# TC big O notation is O(logN)


#(always in log based 2) for 8 item = O(logn) = O(log8) = O(log2^3) = we will find item in 3(maximum/worst case) iteration 
#https://www.youtube.com/watch?v=IR_S8BC8KI0&list=PLeo1K3hjS3uu_n_a__MI_KktGTLYopZ12&index=3