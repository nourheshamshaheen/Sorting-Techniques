# Sorting-Techniques

Assignment for the Data Structures II course in AU. Contributors: Nour Hesham, Lara Hossam

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

Code snippets:
```
def quicksort(array, start, end):
  if len(array) == 1: #base case
  return array
  if start < end:
  q = randomized_partition(array, start, end) #get randomized pivot and
  partition around it
  quicksort(array, start, q-1) #recurse on part of array smaller than pivot
  quicksort(array, q+1, end) #recurse on part of array greater than pivot
  
def randomized_partition(array, start, end):
  i = random.randint(start, end) #choose random element and swap it with end
  array[end], array[i] = array[i], array[end]
  return partition(array, start, end) #call partition on modified array

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

