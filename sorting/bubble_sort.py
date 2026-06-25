'''implement bubble sort'''

'''IDEA --> continuously swap the adjacent elements as per the sorting order. 
If ascending and arr[i] > arr[i+1], swap each other and go similar way for the descending order
compare and swap the elements till all the elements are in the correct sorted order'''

# Repeatedly compare adjacent elements and swap them if they are in the wrong order. 
# After each pass, the largest unsorted element moves to its correct position at the end, effectively "bubbling up."

# MY WAY - like heavy particles (bubbles) sit on the floor and the lighter comes to the surface - we need to do the same. find heavier bubbles and take them down (in ascending)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swap elements

arr = [5, 3, 2, 1, 6, 2, -1, 0, 1]
print("unsorted arr: ", arr)
bubble_sort(arr)
print("sorted array: ", arr)


# TIME COMPLEXITY - O(n^2) where n = size of the array
            # BEST CASE = AVG CASE = WORST CASE --> O(n^@)
# SPACE COMPLEXITY - O(1) - no extra space required, just the normal variables.
# STABLE - YES -> maintains the order of the elements after sorting --> In-place swapping



"""OPTIMIZATION --> if the flag 'swapped' is added, then for the best case (when array is already sorted) - 
we can update the flag and the sorting will be done only in one pass - reducing the time complexity from O(n^2) to O(n)"""
def bubble_sort(arr):
    n = len(arr)
    swapped = false
    for i in range(n-1, -1, -1):
        for j in range(i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]     # swap elements
                swapped = true
        if not swapped:     # if no element is swapped --> array already sorted
            break

arr = [5, 3, 2, 1, 6, 2, -1, 0, 1]
print("unsorted arr: ", arr)
bubble_sort(arr)
print("sorted array: ", arr)


# TIME COMPLEXITY -
            # BEST CASE = O(n)  --> only single pass
            #AVG CASE = WORST CASE --> O(n^@)
# SPACE COMPLEXITY - O(1) - no extra space required, just the normal variables.
# STABLE - YES -> maintains the order of the elements after sorting --> In-place swapping
