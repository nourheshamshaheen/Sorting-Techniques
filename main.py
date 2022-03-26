import random
import time
import matplotlib.pyplot as plt

def quicksort(array, start, end):
    if len(array) == 1: #base case
        return array
    if start < end:
        q = randomized_partition(array, start, end) #get randomized pivot and partition around it
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
    return i+1


def merge_sort(array, start, end):
    if start < end:
        mid = start + (end - start) // 2  #same as (start + end)//2 but to prevent overflow
        merge_sort(array, start, mid) #recurse on left part of array
        merge_sort(array, mid + 1, end) #recurse on right part of array
        merge(array, start, mid, end) #combining step

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

def selection_sort(array):
    for j in range(0, len(array)):
        minIndex = j
        for i in range(j+1, len(array)): #loop on elements, find smallest, put it at i then increment i
            if array[i] < array[minIndex]:
                minIndex = i
        array[minIndex], array[j] = array[j], array[minIndex]#swap smallest element with current element

def selection_sort_modified(array, start, end):
    for j in range(start, end+1):
        minIndex = j
        for i in range(j+1, end+1): #loop on elements, find smallest, put it at i then increment i
            if array[i] < array[minIndex]:
                minIndex = i
        array[minIndex], array[j] = array[j], array[minIndex]


def insertion_sort(array):
    for i in range(1, len(array)): #assume first element is in right position and insert around it
        key = array[i] #holder for next element
        j = i
        while j > 0 and array[j - 1] > key: #move elements of array before key that are greater than key to position after it
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        array[j] = key


def hybrid_merge_sort(array, start, end, threshold):
    if start < end :
        if end - start  <= threshold:
            selection_sort_modified(array, start, end)
        else:
            mid = start + (end - start) // 2
            hybrid_merge_sort(array, start, mid, threshold)
            hybrid_merge_sort(array, mid + 1, end, threshold)
            merge(array, start, mid, end)

def generate_array(size, max):
    array = []
    for i in range(1, size):
        array.append(random.randint(0, max))
    return array

if __name__ == '__main__':
    choice = input("Choose: 1- Run like report (can take a lot of time), 2- Normal Run ")
    choice = int(choice)

    if choice == 1:
        sizes = [1000, 25000, 50000, 75000, 100000]
        quicksort_times = []
        merge_sort_times = []
        selection_sort_times = []
        insertion_sort_times = []

        for size in sizes:
            a = generate_array(size, 1000)
            a1 = a.copy()
            a2 = a.copy()
            a3 = a.copy()
            n = len(a)

            start = time.time()
            quicksort(a, 0, n - 1)
            end = time.time()
            quicksort_times.append(end-start)
            print(*['Time elapsed for quicksort = ', end - start])

            start = time.time()
            merge_sort(a1, 0, n - 1)
            end = time.time()
            merge_sort_times.append(end-start)
            print(*['Time elapsed for mergesort = ', end - start])

            start = time.time()
            selection_sort(a2)
            end = time.time()
            selection_sort_times.append(end-start)
            print(*['Time elapsed for selection sort = ', end - start])

            start = time.time()
            insertion_sort(a3)
            end = time.time()
            insertion_sort_times.append(end-start)
            print(*['Time elapsed for insertion sort = ', end - start])

        # plot lines
        plt.plot(sizes, quicksort_times, label="Quicksort")
        plt.plot(sizes, merge_sort_times, label="Mergesort")
        plt.plot(sizes, selection_sort_times, label="Selection Sort")
        plt.plot(sizes, insertion_sort_times, label="Insertion Sort")
        plt.legend()
        plt.show()

    elif choice == 2:
        size = int(input("Enter array size: "))
        max_value = int(input("Enter max value of values in array: "))
        sort = int(input("Which sort? 1- Quick 2- Merge 3- Selection 4 - Insertion 5- ALL"))
        a = generate_array(size, max_value)
        n = len(a)


        if sort == 1:
            start = time.time()
            quicksort(a, 0, n-1)
            end = time.time()
            print("Time elapsed for quicksort:" + str(end-start))

        elif sort == 2:
            start = time.time()
            merge_sort(a, 0, n-1)
            end = time.time()
            print("Time elapsed for mergesort:" + str(end-start))
        elif sort == 3:
            start = time.time()
            selection_sort(a, 0, n-1)
            end = time.time()
            print("Time elapsed for selection sort:" + str(end-start))
        elif sort == 4:
            start = time.time()
            insertion_sort(a, 0, n-1)
            end = time.time()
            print("Time elapsed for insertion sort:" + str(end-start))
        elif sort == 5:
            a1 = a.copy()
            a2 = a.copy()
            a3 = a.copy()
            n = len(a)
            start = time.time()
            quicksort(a, 0, n - 1)
            end = time.time()
            print(*['Time elapsed for quicksort = ', end - start])

            start = time.time()
            merge_sort(a1, 0, n - 1)
            end = time.time()
            print(*['Time elapsed for mergesort = ', end - start])

            start = time.time()
            selection_sort(a2)
            end = time.time()
            print(*['Time elapsed for selection sort = ', end - start])

            start = time.time()
            insertion_sort(a3)
            end = time.time()
            print(*['Time elapsed for insertion sort = ', end - start])

        else:
            print("Wrong choice.")
