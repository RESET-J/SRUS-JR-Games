# In your own words, describe what sorting is in general. 
> Sorting is the process of arranging or rearanging elements in an list in an specific way or order, such as acsending / descending, for example sorting alphabetically would be sorting an list of values by ascending order, A, B, C, ect.., or if by descending C, B, A, ect...

# Research sorting algorithms. Describe advantages and disadvantages for at least three different sorting algorithms. Please provide references for external resources.

> ### Bubble Sort
> Bubble sort is an algorithm that sorts by comparing two elements that are adjacent, and then swaping them based on the comparison until they are all in the specified order

> Advantages - simple to understand, easy to impliment, the bubble sort algorithm swaps elements in place without using aditional temporary storage, this makes the space requirement low

> Disadvantages - This algorithm is not ideal for sorting large amounts of data, as the time complexity of this algorithm is O(n^2) each element in the list will affect the performance of this algorithm

> https://sciencing.com/the-advantages-disadvantages-of-sorting-algorithms-12749529.html
https://www.programiz.com/dsa/bubble-sort

> ### Selection Sort
> Selection sort goes repetedly trough each of the elements in an list and selects an item according to its ordering / placing, and puts it in the correct position

> Advantages - This algorithm performs well on small lists, no additional temporary storage is required.

> Disadvantages - Like the bubble sorting algroithm this sorting algorithm is not ideal for large amounts of data, as this algorithm also has an time complexity of o(n^2).

> https://sciencing.com/the-advantages-disadvantages-of-sorting-algorithms-12749529.html
https://www.programiz.com/dsa/selection-sort

> ### Quick Sort
> Quick sort works on an "Divide and Conquer" principle, the quick sort algorithm selects an pivot element, elements are then divided into subarrays with the elements that are less than the pivot kept on the left and elements higher than the pivot on the right, this process continues until all elements in the list are sorted.

> Advantages - This algorithm is very efficient and is often considered as one of the best sorting algorithms,it is able to sort lists with an large amount of data / items with ease, as this sorts inplace it also has the same advatages as bubblesort where no aditional temporary storage is required

> Disadvatages - Worst case scenarios can lower the performance to that / similar of the bubble sorting algorithm.

> https://sciencing.com/the-advantages-of-heap-sort-12749895.html
https://www.programiz.com/dsa/quick-sort

# In your own words, describe why you generally need comparison operators to successfully sort a list of objects. In addition, describe how you could sort a list of objects without adding comparison operators

> Comparison operators are generally needed when sorting through values, so that objects / values can be compared to each other, for example determining whether A is greater than B ( or B is greater than A ) or for integers such as 1 is less than 2, many sorting algorithms use this to determine if the elment is in the correct position.

> In majority of cases sorting requires comparison operators however there are sorting algorithms that do not need this, such as counting sort / redix sort. An way that you could sort an array of elements without comparison operators, is to use an array of elements as an index, then store the counts in an array, treverse the list and print elements its count times.

> An example of sorting an array of integers with this method, from -geeksforgeeks.org

```python
# Python3 program to sort an array without comparison
# operator.
 
def sortArr(arr, n, min_no, max_no):
    # Count of elements in given range 
    m = max_no - min_no + 1
     
    # Count frequencies of all elements
    c = [0] * m
    for i in range(n):
        c[arr[i] - min_no] += 1
 
    # Traverse through range. For every
    # element, print it its count times.
    for i in range(m):
        for j in range((c[i])):
            print((i + min_no), end=" ")
 
# Driver Code
arr = [10, 10, 1, 4, 4, 100, 0]
min_no,max_no = 0,100
n = len(arr)
sortArr(arr, n, min_no, max_no)
 
# This code is contributed by Rajput-Ji
# Improved by Rutvik J
```

> GeeksforGeeks. (2018). Sorting without comparison of elements. [online] Available at: https://www.geeksforgeeks.org/sorting-without-comparison-of-elements/.

# Choose an algorithm of your liking based on the answers you provided to the Knowledge Questions and describe why you chose it
> I chose the quick sort algorithm, as it is better for large amounts of items, and is considered one of the best algorithms for efficiency.