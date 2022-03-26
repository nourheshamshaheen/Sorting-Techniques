# Sorting-Techniques

Assignment for the Data Structures II course in Alexandria University. Contributors: Nour Hesham, Lara Hossam

## Abstract
Sorting is one of the most fundamental algorithmic problems within computer science. It
has been claimed that as many as 25% of all CPU cycles are spent sorting, which provides a
lot of incentive for further study and optimization of sorting. In addition, there are many
other tasks (searching, calculating the median, finding the mode, removing duplicates, etc.)
that can be implemented much more efficiently once the data is sorted. The wide variety of
algorithms gives us a lot of richness to explore, especially when considering the tradeoffs
offered in terms of efficiency, operation mix, code complexity, best/worst case inputs, and
so on.

## Quick Sort: Implementation of QuickSort algorithm using randomized partitioning:
QuickSort is a divide and conquer algorithm, it picks an element as a pivot (in this case, the
element is chosen randomly using the randint() function.), and then partitions the given
array around the picked pivot.
The process is as follows:
1) The array is partitioned into two sub-arrays around pivot x such that all left
elements are smaller than x and all right elements are greater than x.
2) Recursively sorts the two sub-arrays.
3) Combine both sub-arrays.

**Partitioning algorithm:**
We start from the leftmost index and keep track of the number of smaller/equal elements
than the pivot (last element of the array) in the variable i, if we find a smaller/equal
element, it is swapped with array of index i, otherwise, we ignore the current element and i
isn’t incremented. At the end, the pivot is swapped with the element of index i+1, as it’s its
correct position in the array, and recursively each of the two formed sub-arrays is traversed
and changed.

**Code snippets:**
```
def quicksort(array, start, end):
  if len(array) == 1: #base case
  return array
  if start < end:
  q = randomized_partition(array, start, end) #get randomized pivot and
  partition around it
  quicksort(array, start, q-1) #recurse on part of array smaller than pivot
  quicksort(array, q+1, end) #recurse on part of array greater than pivot
```

```  
def randomized_partition(array, start, end):
  i = random.randint(start, end) #choose random element and swap it with end
  array[end], array[i] = array[i], array[end]
  return partition(array, start, end) #call partition on modified array
```

```
def partition(array, start, end):
  i = start-1
  x = array[end] #choose end element as pivot
  for j in range(start, end): #loop on elements
    if array[j] <= x:
      i = i+1 #indicates right position of pivot so far and number of elements smaller than pivot
      array[j], array[i] = array[i], array[j] #swap current element with element smaller than pivot
  array[i+1], array[end] = array[end], array[i+1] #put pivot in its correct place
  return i+15
```
## Merge Sort: Implementation of MergeSort algorithm
Merge Sort is a divide and conquer sorting algorithm, it divides the input array into two
halves and calls itself recursively to sort each of those halves and then combines them
together along with sorting.
The process is as follows:
1) The middle index is found and the array is subdivided into two sub arrays
2) Each of the two halves is broken down into single elements via recursively calling the
mergeSort() function.
3) The conquer part is using the merge() function that sorts every sub-array and
merges it with the next one until the final array is completely sorted.

**Merging algorithm:**
The merge sort is all about the merging algorithm, it breaks the array into two sub-arrays
stored temporarily in L[] and R[] recursively until every element is compared to the one
next to it, they’re stored correctly and recursively combines the individual arrays until the
last one is completely sorted.

**Code Snippets:**
```
def merge(array, start, mid, end):
  size1 = mid - start + 1
  size2 = end - mid
  L = [0] * (size1) #initialize L array with zeros
  R = [0] * (size2) #initialize R array with zeros
  for i in range(0, size1): #copy left part of main array to L
    L[i] = array[start+i]
  for i in range(0, end-mid): #copy right part of main array to R
    R[i] = array[mid+i+1]
  
  i = 0
  j = 0
  k = start
  #merge both arrays: put elements in order in main array
  while i < size1 and j < size2:
    if L[i] <= R[j]:
      array[k] = L[i]
      i = i+1
    else:
      array[k] = R[j]
      j = j+1
    k = k+1
  #if one array is bigger than the other
  while i < size1:
    array[k] = L[i]
    i = i+1
    k = k+1
  while j < size2:
    array[k] = R[j]
    j = j+1
    k = k+1
 ```

## Selection Sort: Implementation of Selection Sort algorithm
```
def selection_sort(array):
  for j in range(0, len(array)):
    minIndex = j
  for i in range(j+1, len(array)):  # loop on elements, find smallest, put it at i then increment i
    if array[i] < array[minIndex]:
    minIndex = i
  array[minIndex], array[j] = array[j], array[minIndex]  # swap smallest element with current element
```

## Insertion Sort: Implementation of Insertion Sort algorithm
```
def insertion_sort(array):
  for i in range(1, len(array)): # assume first element is in right position and insert around it
    key = array[i] #holder for next element
    j = i
    while j > 0 and array[j - 1] > key: # move elements of array before key that are greater than key to position after it
      array[j - 1], array[j] = array[j], array[j - 1]
      j -= 1
    array[j] = key
```
## Time Comparison Report

| Algorithm   | n = 1000 | n = 25000 | n = 50000 | n = 75000 | n = 100000 |
| ----------- | ---------| --------- | --------- | --------- | --------- |
| Quick | 0.0 | 0.2298 | 0.9018 | 1.6782 | 2.5633 |
| Merge | 0.009 | 0.2497 | 0.6565 | 0.8779 | 1.3132 |
| Selection | 0.0599 | 45.917 | 194.282 | 457.412| 633.3568 |
| Insertion | 0.0899| 75.925 | 322.864 | 768.602 | 984.9915 |


## Hybrid Merge and Selection Algorithm 
```
def hybrid_merge_sort(array, start, end, threshold):
  if start < end :
    if end - start <= threshold:
    selection_sort_modified(array, start, end)
  else:
    mid = start + (end - start) // 2
    hybrid_merge_sort(array, start, mid,threshold)
    hybrid_merge_sort(array, mid + 1, end,threshold)
    merge(array, start, mid, end)
```

## Find kth element in an unsorted array
```
def kth_smallest(array, start, end, k):
  if start >= end:
    return array[start]
  pivot = randomized_partition(array, start, end) #partition around pivot
  rank = pivot-start+1 #get rank of pivot (if start doesn't equal 0)
  if rank == k: #if rank of pivot is the same as demanded
    return array[pivot]
  elif rank < k: #if rank of pivot smaller than demanded recurse on right part of array while changing k to be k-rank
    return kth_smallest(array, pivot+1, end, k-rank)
  else: #if rank of pivot greater than demanded recurse on left part of array
    return kth_smallest(array, start, pivot-1, k)
```




