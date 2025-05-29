stock_price = [250, 253, 255, 260, 257, 255]

# java and C++ has both static and dynamic array, dynamic array uses geometric progression; new array = array * 2 and copy old element to it; python can store multiple type of item in a array but java and C++ can not
# python uses object and references for memory representation

# #1 look up by index O(1)
# rd = stock_price[2]
# print(rd)

# #2 On what day price was 260 O(n)
# for i in range(len(stock_price)):
#     if stock_price[i] == 260:
#         print(i)

# #3 printing all the value O(n)
# for price in stock_price:
#     print(price)

# #4 inserting in array, it insert and shift existing values(since in python array is dynamic(list)) so it takes O(n)
# stock_price.insert(1,300)

# print(stock_price)

# #5 deleting; it delete and shift other takes O(n)
# print(stock_price)

# stock_price.pop(1)#for item in index 1
# print(stock_price)

# #if there are duplicate in the array first item from left get deleted
# stock_price.remove(255)#for value

# print(stock_price)

# 6  2-dimentional array
stock_price = [
    [2, 3, 5, 6],
    [6, 9, 5, 1],
    [6, 4, 8, 2, 3]
]

# 7 Exercise 1
ex = [2000, 2200, 2350, 2000, 2600, 2130, 2190]

# q1 WAP difference of expenses between January and February
# fj = ex[1] - ex[0]
# print(f'{fj} more dollar was spended in February in compare to Janauary')


# q2  WAP sum of first 3 expenses
# qs = 0

# for i in range(3):
#     qs += ex[i]
# print(qs)

# #or

# qsum = sum(ex[:3])
# print(qsum)

# p = ex[:-1]#gives except last element
# print(p)

# #q3 Find exactly in which month did you spend 2000
# #else block inside for loop execute in every loop run so used another method
months = ['January', "February", "March", "April", "May"]

# found = False

# for i in range(len(ex)):

#     if ex[i] == 2000:
#         month = months[i]
#         print(f"yes you have spend 2000 in {month}")
#         found = True

# if not found:
#     print("No, you have not spend exactly 2000 in any month")

#OR
#print("Did I spent 2000$ in any month? ", 2000 in ex) # True/FAlSE = O/P

# #q4 add expenses of june
# months.append("June")

# ex.append(1980)

# print(ex)

# q5 WAP decrease the expenses of April by 200 (updating)

# paex = ex[3]

# naex = paex - 200

# ex.insert(3, naex)#insert used to add element to specific position while append to add at the end of the array

# print(ex)

# #OR
# print(ex)
# ex[3] = ex[3] - 200
# print(ex)


# Exercise 2

