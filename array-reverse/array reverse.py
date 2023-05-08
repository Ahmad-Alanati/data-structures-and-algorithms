
def reverse_array(arr):
    if len(arr) <= 1:
        return arr
    else:
        return reverse_array(arr[1:]) + [arr[0]]
    
arr = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 4, 5, 6]
arr3 = [89, 2354, 3546, 23, 10, -923, 823, -12]
arr4 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
         79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199]

print(reverse_array(arr))
print(reverse_array(arr2))
print(reverse_array(arr3))
print(reverse_array(arr4))