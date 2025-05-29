def print_triplets(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                print(arr[i], arr[j], arr[k])

print_triplets([1, 2, 3, 4])

# 3 nested loop iterate N*N*N times
# TC = O(N^3)