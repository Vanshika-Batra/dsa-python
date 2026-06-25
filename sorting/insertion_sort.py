'''implement insertion sort'''

'''IDEA --> 2 parts - sorted and unsorted. Iterate the unsorted array, for all the elements in the unsorted array
find the correct place to insert in the sorted array'''

# sorting - ascending order
def insertion_sort(arr):
    n = len(arr)
    # single element is always sorted - arr[0] - is sorted
    for i in range(1, n):   # unsorted array
        unsorted_element = arr[i]
        j = i -1
        while j >=0 and unsorted_element<arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = unsorted_element     # place the unsorted element at its correct sorted place

arr = [5, 3, 2, 1, 6, 2, -1, 0, 1]
# arr = [1,2,3,4,4]
print("unsorted arr: ", arr)
insertion_sort(arr)
print("sorted array: ", arr)


# TIME COMPLEXITY - O(n^2) where n = size of the array
            # BEST CASE = O9N) - when the array is sorted - single pass is required 
            # AVG CASE = WORST CASE --> O(n^2)
# SPACE COMPLEXITY - O(1) - no extra space required, just the normal variables.
# STABLE - YES -> maintains the order of the elements after sorting -> relative order of the same elements is maintained
# In-place swapping -- no extra memory is required