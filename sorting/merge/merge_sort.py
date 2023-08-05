
def merge_sort(arr):
    length = len(arr)
    if length == 1:
        return arr

    mid = int(length/2)
    left = arr[0:mid]
    right = arr[mid:length]
    left = merge_sort(left)
    right = merge_sort(right)
    sorted_array = []
    merge(left,right,sorted_array)
    return sorted_array
    


def merge(left,right,array):
    i = j = k = 0
    while i<len(left) and j <len(right):
        if left[i]<=right[j]:
            array.append(left[i])
            i+=1
        else:
            array.append(right[j])
            j+=1
        k+=1

    if i == len(left):
        while j!= len(right):
            array.append(right[j])
            j+=1
    else:
        while i!= len(left):
            array.append(left[i])
            i+=1

if __name__ == "__main__":
    array = [2,3,5,7,13,11]
    sorted_array = merge_sort(array)
    print(sorted_array)