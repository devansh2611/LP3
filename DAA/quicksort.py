
import random


def quicksort(arr, low, high):
    if(low < high):
        pivotindex = partitionrand(arr,low, high)
        
        quicksort(arr , low , pivotindex)
        quicksort(arr, pivotindex + 1, high)


def partitionrand(arr , low, high):
    randpivot = random.randrange(low, high)
    
    arr[low], arr[randpivot] = arr[randpivot], arr[low]
    return partition(arr, low, high)


def partition(arr,low,high):
    pivot = low # pivot
    i = low - 1
    j = high + 1
    while True:
        while True:
            i = i + 1
            if arr[i] >= arr[pivot]:
                break
        while True:
            j = j - 1
            if arr[j] <= arr[pivot]:
                break
        if i >= j:
            return j
        arr[i] , arr[j] = arr[j] , arr[i]
        
array = [10, 7, 8, 9, 1, 5]
quicksort(array, 0, len(array) - 1)
print(array)
