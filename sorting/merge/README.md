# merge Sort

merge sort is a sorting algorithm it traverses the unsorted array and insert the element in an new array in a sorted order before returning it.

```pseudocode
ALGORITHM Mergesort(arr)
    DECLARE n <-- arr.length

    if n > 1
      DECLARE mid <-- n/2
      DECLARE left <-- arr[0...mid]
      DECLARE right <-- arr[mid...n]
      // sort the left side
      Mergesort(left)
      // sort the right side
      Mergesort(right)
      // merge the sorted left and right sides together
      Merge(left, right, arr)

ALGORITHM Merge(left, right, arr)
    DECLARE i <-- 0
    DECLARE j <-- 0
    DECLARE k <-- 0

    while i < left.length && j < right.length
        if left[i] <= right[j]
            arr[k] <-- left[i]
            i <-- i + 1
        else
            arr[k] <-- right[j]
            j <-- j + 1

        k <-- k + 1

    if i = left.length
       set remaining entries in arr to remaining values in right
    else
       set remaining entries in arr to remaining values in left
```

## Trace

### first example

Sample array: [8,4,23,42,16,15]

- step 1

![step1](./steps%20images/step1.jpg)

in step 1 we split the array to two half right and left then we call the function Mergesort again with the left array

- step 2

![step2](./steps%20images/step2.jpg)

in step 2 we split the array to two half right and left then we call the function Mergesort again with the left array but the left has one element so it will do nothing then call the Mergesort with the right array

- step 3

![step3](./steps%20images/step3.jpg)

in step 3 we split the array to two half right and left then we call the function Mergesort again with the left array but the left has one element so it will do nothing then call the Mergesort with the right array and it has one element so it will go and call the merge function

- step 4

![step4](./steps%20images/step4.jpg)

in step 4 we combine the left and the right then return it so 4 is less then 23 so we add 4 to a new array then we add 23 to the array, after that return the new array. 

- step 5

![step5](./steps%20images/step5.jpg)

in step 5 we combine the left and the right then return it so 8 is greater then 4 so we add 4 to a new array then we add 8 to the array and 23 will be add last, after that return the new array. 

- step 6

![step6](./steps%20images/step6.jpg)

in step 6 we split the array to two half right and left then we call the function Mergesort again with the left array but the left has one element so it will do nothing then call the Mergesort with the right array

- step 7

![step7](./steps%20images/step7.jpg)

in step 7 we split the array to two half right and left then we call the function Mergesort again with the left array but the left has one element so it will do nothing then call the Mergesort with the right array and it has one element so it will go and call the merge function

- step 8

![step8](./steps%20images/step8.jpg)

in step 8 we combine the left and the right then return it so 16 is greater then 15 so we add 15 to a new array then we add 16 to the array, after that return the new array. 

- step 9

![step9](./steps%20images/step9.jpg)

in step 9 we combine the left and the right then return it so 42 is greater then 15 so we add 15 to a new array then we add 16 to the array and lastly 42, after that return the new array. 

- step 10

![step10](./steps%20images/step10.jpg)

in step 10 we combine the left and the right then return it so 4 is less then 15 so we add 4 to a new array then we add 8 to the array after that we add 15 and 16,23,42, after that we return the orderd array. 

## Efficency

- Time:O(n log n):
  - the basic operation of this algorithm is comparison. this will happen n time that is why it will take n log n to finish sorting the array why n log n because it will run the merge opration like a tree that is why it will take log n to merge the array.

- space: O(n)
  - because the algorithm is reserving a call stack.