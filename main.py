import random

def quicksort(array, start, end):
    if len(array) == 1:
        return array
    if start < end:
        q = randomized_partition(array, start, end)
        quicksort(array, start, q-1)
        quicksort(array, q+1, end)

def randomized_partition(array, start, end):
    i = random.randint(start, end)
    array[start], array[i] = array[i], array[start]
    return partition(array, start, end)

def partition(array, start, end):
    i = start-1
    x = array[end]
    for j in range(start, end):
        if array[j] <= x:
            i = i+1
            array[j], array[i] = array[i], array[j]
    array[i+1], array[end] = array[end], array[i+1]
    return i+1

def merge_sort(array, start, end):
    if start < end:
        mid = start + (end - start) // 2
        merge_sort(array, start, mid)
        merge_sort(array, mid + 1, end)
        merge(array, start, mid, end)

def merge(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0, n1):
        L[i] = array[start+i]
    for i in range(0, end-mid):
        R[i] = array[mid+i+1]
    i = 0
    j = 0
    k = start
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            array[k] = L[i]
            i = i+1
        else:
            array[k] = R[j]
            j = j+1
        k = k+1

    while i < n1:
        array[k] = L[i]
        i = i+1
        k = k+1

    while j < n2:
        array[k] = R[j]
        j = j+1
        k = k+1

def kth_smallest(array, start, end, k):
    if start >= end:
        return array[start]
    r = randomized_partition(array, start, end)
    i = r-start+1
    if i == k:
        return array[r]
    elif i < k:
        return kth_smallest(array, r+1, end, k-i)
    else:
        return kth_smallest(array, start, r-1, k)

def generate_array(size):
    array = []
    for i in range(1, size):
        array.append(random.randint(0, 1000))
    return array


def selectionSort(array):
    for j in range(0, len(array) - 1):
        minIndex = j
        for i in range(j, len(array)):
            if array[i] < array[minIndex]:
                minIndex = i
                i += 1
            if minIndex != j:
                array[minIndex], array[j] = array[j], array[minIndex]


def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i
        while j > 0 and array[j - 1] > key:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        array[j] = key


if __name__ == '__main__':
    a = [1, 4, 5, 8, 0, 2, 3]
    n = len(a)
    print(str(n))
    b = kth_smallest(a, 0, n-1, 2)
    quicksort(a, 0, n-1)
    print(str(b))




