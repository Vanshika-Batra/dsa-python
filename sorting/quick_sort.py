'''implement quick sort'''

'''IDEA --> Divide & Conquer
in this elements are maintained as per the pivot/partition point. In case of ascending order, the elements in the left of the 
pivot point are all lesser than the pivot point and those to its right are greater or equal to the pivot point
The left and right sides are not necessarily sorted.
Only the pivot reaches its final correct position.'''


# Quick Sort follows the Divide and Conquer paradigm.
# A pivot element is selected.
# The array is partitioned so that elements smaller than
# the pivot are placed on its left and larger elements on its right.
# The same process is recursively applied to both partitions.
# Eventually the entire array becomes sorted.

def partition(arr, start, end):
    pivot = arr[end]
    i = start -1
    for j in range(start, end):
        if arr[j]<=pivot:
            i +=1
            arr[i], arr[j] = arr[j], arr[i]     # place smaller/equal elements on the left side
    arr[i+1], arr[end] = arr[end], arr[i+1]   # swap the pivot point - to get its correct position
    return i+1      # pivot point (partition index)

def quick_sort(arr, start, end):
    if start >= end:
        return 
    index = partition(arr, start, end)
    quick_sort(arr, start, index-1)
    quick_sort(arr, index+1, end)


arr = [5, 3, 2, 1, 6, 2, -1, 0, 1]
# arr = [1,2,3,4,4]
print("unsorted arr: ", arr)
quick_sort(arr, 0, len(arr)-1)
print("sorted array: ", arr)


# TIME COMPLEXITY -
            # BEST CASE (when pivot is somewhere in the middle)= AVG CASE  --> O(n*logn)
            # WORST CASE = O(n^2) - when array is already sorted, and pivot is the last/first element

# SPACE COMPLEXITY - 
# | Case    | Space    |
# | ------- | -------- |
# | Best    | O(log n) |
# | Average | O(log n) |
# | Worst   | O(n)     |


# STABLE - NO  -> Partition swaps can produce: order changed -> relative order of the same elements is maintained
# In-place swapping -- no extra memory is required  --> An algorithm is in-place if it uses only O(1) extra memory.