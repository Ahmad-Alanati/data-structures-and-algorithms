import math

def insertShiftArray(arr, element):
    newarr = []
    for i in range(math.ceil(len(arr)/2)):
        newarr.append(arr[i])
    newarr.append(element)
    for i in range(math.ceil(len(arr)/2),len(arr)):
        newarr.append(arr[i])
    return newarr

def remove_middle_element(arr):
    newarr = []
    if len(arr) == 1:
        return []
    if len(arr)%2==0 :
        for i in range(len(arr)):
            if i==len(arr)/2-1 or i ==len(arr)/2:
                continue
            newarr.append(arr[i])
    else:
        for i in range(len(arr)):
            if i == math.floor(len(arr)/2):
                continue
            newarr.append(arr[i])
    return newarr


