arr1 = [2,36,4,8,95,3,2,4,6,8,5]

def check_duplicate(arr):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                #print(f'found duplicate {arr[i]} at {i} and {j} positions')
                return True
    return False

#check_duplicate(arr1)
print(check_duplicate(arr1))

# 2 nested loop operated over N*N elments
# O(N^2)

