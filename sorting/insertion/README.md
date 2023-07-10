# Insertion Sort

insertion sort is a sorting algorithm it traverses the unsorted array and insert the element in an new array in a sorted order before returning it.

```pseudocode
Insert(int[] sorted, int value)
  initialize i to 0
  WHILE value > sorted[i]
    set i to i + 1
  WHILE i < sorted.length
    set temp to sorted[i]
    set sorted[i] to value
    set value to temp
    set i to i + 1
  append value to sorted

InsertionSort(int[] input)
  LET sorted = New Empty Array
  sorted[0] = input[0]
  FOR i from 1 up to input.length
    Insert(sorted, input[i])
  return sorted
```

## Trace

### first example

Sample array: [8,4,23,42,16,15]

- step 1

![step1](./steps%20images/step1.jpg)

in step 1 we create and add the first element of the unsorted array to the sorted array and create a variable called i = 1 to loop thought the unsroted array

- step 2

![step2](./steps%20images/step2.jpg)

in step 2 we enter the loop and call the function called insert with the sorted array and 4(second element) in the unsorted array, after it finish the sorted array will add 4 before the 8

- step 3

![step3](./steps%20images/step3.jpg)

in step 3  we increase the i by 1 and call the function insert again with the sorted array and 23(third element) in the unsorted array, after it finish the sorted array will add the 23 at the end of the array

- step 4

![step4](./steps%20images/step4.jpg)

in step 4 we increase the i by 1 and call the function insert again with the sorted array and 42(fourth element) in the unsorted array, after it finish the sorted array will add the 42 at the end of the array

- step 5

![step5](./steps%20images/step5.jpg)

in step 5 we increase the i by 1 and call the function insert again with the sorted array and 16(fifth element) in the unsorted array, after it finish the sorted array will add the 16 before 23

- step 6

![step6](./steps%20images/step6.jpg)

in step 6 we increase the i by 1 and call the function insert again with the sorted array and 15(sixth element) in the unsorted array, after it finish the sorted array will add the 15 before 16

### second example

Sample array: [20,18,12,8,5,-2]

- step 1

![step1](./steps%20images/step1_ex2.jpg)

in step 1 we create and add the first element of the unsorted array to the sorted array and create a variable called i = 1 to loop thought the unsroted array

- step 2

![step2](./steps%20images/step2_ex2.jpg)

in step 2 we enter the loop and call the function called insert with the sorted array and 18(second element) in the unsorted array, after it finish the sorted array will add 18 before the 20

- step 3

![step3](./steps%20images/step3_ex2.jpg)

in step 3  we increase the i by 1 and call the function insert again with the sorted array and 12(third element) in the unsorted array, after it finish the sorted array will add the 12 before the 18

- step 4

![step4](./steps%20images/step4_ex2.jpg)

in step 4 we increase the i by 1 and call the function insert again with the sorted array and 42(fourth element) in the unsorted array, after it finish the sorted array will add the 8 before the 12

- step 5

![step5](./steps%20images/step5_ex2.jpg)

in step 5 we increase the i by 1 and call the function insert again with the sorted array and 5(fifth element) in the unsorted array, after it finish the sorted array will add the 5 before 8

- step 6

![step6](./steps%20images/step6_ex2.jpg)

in step 6 we increase the i by 1 and call the function insert again with the sorted array and -2(sixth element) in the unsorted array, after it finish the sorted array will add the -2 before 5

### third example

Sample array: [5,12,7,5,5,7]

- step 1

![step1](./steps%20images/step1_ex3.jpg)

in step 1 we create and add the first element of the unsorted array to the sorted array and create a variable called i = 1 to loop thought the unsroted array

- step 2

![step2](./steps%20images/step2_ex3.jpg)

in step 2 we enter the loop and call the function called insert with the sorted array and 12(second element) in the unsorted array, after it finish the sorted array will add the 12 at the end of the array

- step 3

![step3](./steps%20images/step3_ex3.jpg)

in step 3  we increase the i by 1 and call the function insert again with the sorted array and 7(third element) in the unsorted array, after it finish the sorted array will add the 7 before the 12

- step 4

![step4](./steps%20images/step4_ex3.jpg)

in step 4 we increase the i by 1 and call the function insert again with the sorted array and 5(fourth element) in the unsorted array, after it finish the sorted array will add the 5 before the 7

- step 5

![step5](./steps%20images/step5_ex3.jpg)

in step 5 we increase the i by 1 and call the function insert again with the sorted array and 5(fifth element) in the unsorted array, after it finish the sorted array will add the 5 before 7

- step 6

![step6](./steps%20images/step6_ex3.jpg)

in step 6 we increase the i by 1 and call the function insert again with the sorted array and 7(sixth element) in the unsorted array, after it finish the sorted array will add the 7 before 12


### fourth example

Sample array: [2,3,5,7,13,11]

- step 1

![step1](./steps%20images/step1_ex4.jpg)

in step 1 we create and add the first element of the unsorted array to the sorted array and create a variable called i = 1 to loop thought the unsroted array

- step 2

![step2](./steps%20images/step2_ex4.jpg)

in step 2 we enter the loop and call the function called insert with the sorted array and 3(second element) in the unsorted array, after it finish the sorted array will add the 3 at the end of the array

- step 3

![step3](./steps%20images/step3_ex4.jpg)

in step 3  we increase the i by 1 and call the function insert again with the sorted array and 5(third element) in the unsorted array, after it finish the sorted array will add the 5 at the end of the array

- step 4

![step4](./steps%20images/step4_ex4.jpg)

in step 4 we increase the i by 1 and call the function insert again with the sorted array and 7(fourth element) in the unsorted array, after it finish the sorted array will add the 7 at the end of the array

- step 5

![step5](./steps%20images/step5_ex4.jpg)

in step 5 we increase the i by 1 and call the function insert again with the sorted array and 13(fifth element) in the unsorted array, after it finish the sorted array will add the 13 at the end of the array

- step 6

![step6](./steps%20images/step6_ex4.jpg)

in step 6 we increase the i by 1 and call the function insert again with the sorted array and 11(sixth element) in the unsorted array, after it finish the sorted array will add the 11 before 13


## Efficency

- Time:O(n^2):
  - the basic operation of this algorithm is comparison. this will happen n*(n-1) that is why it will take n^2 to finish sorting the array.

- space: O(n)
  - because the algorithm is reserving an array and it increases with everytime we call insert function.